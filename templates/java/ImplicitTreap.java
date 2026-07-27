/**
 * Randomized dynamic sequence with split/merge by position.
 *
 * <p>Supports insertion, deletion, lazy range reversal, range sum and range
 * minimum. All positions are zero-based and all ranges are half-open [left, right).
 * Expected time per operation is O(log n).
 */
public final class ImplicitTreap {
    private Node root;
    private long randomState;

    public ImplicitTreap() {
        this(System.nanoTime());
    }

    /** Deterministic seed is useful for stress tests. */
    public ImplicitTreap(long seed) {
        randomState = seed;
    }

    public ImplicitTreap(long[] values) {
        this(values, System.nanoTime());
    }

    public ImplicitTreap(long[] values, long seed) {
        this(seed);
        for (long value : values) root = merge(root, new Node(value, nextPriority()));
    }

    public int size() {
        return size(root);
    }

    public boolean isEmpty() {
        return root == null;
    }

    public long get(int index) {
        checkElementIndex(index);
        Node node = root;
        while (true) {
            push(node);
            int leftSize = size(node.left);
            if (index < leftSize) {
                node = node.left;
            } else if (index == leftSize) {
                return node.value;
            } else {
                index -= leftSize + 1;
                node = node.right;
            }
        }
    }

    public void insert(int index, long value) {
        checkPositionIndex(index);
        Split split = split(root, index);
        root = merge(split.left, merge(new Node(value, nextPriority()), split.right));
    }

    public long remove(int index) {
        checkElementIndex(index);
        Split leftAndRest = split(root, index);
        Split itemAndRight = split(leftAndRest.right, 1);
        long removed = itemAndRight.left.value;
        root = merge(leftAndRest.left, itemAndRight.right);
        return removed;
    }

    public void reverse(int left, int right) {
        checkRange(left, right);
        RangeParts parts = cut(left, right);
        toggleReverse(parts.middle);
        restore(parts);
    }

    public long rangeSum(int left, int right) {
        checkRange(left, right);
        RangeParts parts = cut(left, right);
        long result = sum(parts.middle);
        restore(parts);
        return result;
    }

    /** The range must be non-empty. */
    public long rangeMin(int left, int right) {
        checkRange(left, right);
        if (left == right) throw new IllegalArgumentException("rangeMin requires a non-empty range");
        RangeParts parts = cut(left, right);
        long result = min(parts.middle);
        restore(parts);
        return result;
    }

    public long[] toArray() {
        long[] result = new long[size()];
        fill(root, result, new int[]{0});
        return result;
    }

    private RangeParts cut(int left, int right) {
        Split leftAndRest = split(root, left);
        Split middleAndRight = split(leftAndRest.right, right - left);
        return new RangeParts(leftAndRest.left, middleAndRight.left, middleAndRight.right);
    }

    private void restore(RangeParts parts) {
        root = merge(parts.left, merge(parts.middle, parts.right));
    }

    /** Returns the first leftSize elements and the remaining suffix. */
    private Split split(Node node, int leftSize) {
        if (node == null) return new Split(null, null);
        push(node);
        if (size(node.left) >= leftSize) {
            Split split = split(node.left, leftSize);
            node.left = split.right;
            pull(node);
            return new Split(split.left, node);
        }
        Split split = split(node.right, leftSize - size(node.left) - 1);
        node.right = split.left;
        pull(node);
        return new Split(node, split.right);
    }

    private Node merge(Node left, Node right) {
        if (left == null) return right;
        if (right == null) return left;
        if (Long.compareUnsigned(left.priority, right.priority) > 0) {
            push(left);
            left.right = merge(left.right, right);
            pull(left);
            return left;
        }
        push(right);
        right.left = merge(left, right.left);
        pull(right);
        return right;
    }

    private static void toggleReverse(Node node) {
        if (node != null) node.reversed = !node.reversed;
    }

    private static void push(Node node) {
        if (node == null || !node.reversed) return;
        Node tmp = node.left;
        node.left = node.right;
        node.right = tmp;
        toggleReverse(node.left);
        toggleReverse(node.right);
        node.reversed = false;
    }

    private static void pull(Node node) {
        node.size = size(node.left) + 1 + size(node.right);
        node.sum = sum(node.left) + node.value + sum(node.right);
        node.min = Math.min(node.value, Math.min(min(node.left), min(node.right)));
    }

    private static int size(Node node) {
        return node == null ? 0 : node.size;
    }

    private static long sum(Node node) {
        return node == null ? 0 : node.sum;
    }

    private static long min(Node node) {
        return node == null ? Long.MAX_VALUE : node.min;
    }

    private static void fill(Node node, long[] result, int[] position) {
        if (node == null) return;
        push(node);
        fill(node.left, result, position);
        result[position[0]++] = node.value;
        fill(node.right, result, position);
    }

    private void checkElementIndex(int index) {
        if (index < 0 || index >= size()) throw new IndexOutOfBoundsException(index);
    }

    private void checkPositionIndex(int index) {
        if (index < 0 || index > size()) throw new IndexOutOfBoundsException(index);
    }

    private void checkRange(int left, int right) {
        if (left < 0 || left > right || right > size()) {
            throw new IndexOutOfBoundsException("[" + left + ", " + right + ")");
        }
    }

    /** SplitMix64: fast priorities with a much better distribution than key-based hashes. */
    private long nextPriority() {
        randomState += 0x9E3779B97F4A7C15L;
        long z = randomState;
        z = (z ^ (z >>> 30)) * 0xBF58476D1CE4E5B9L;
        z = (z ^ (z >>> 27)) * 0x94D049BB133111EBL;
        return z ^ (z >>> 31);
    }

    private static final class Node {
        final long priority;
        long value;
        long sum;
        long min;
        int size = 1;
        boolean reversed;
        Node left;
        Node right;

        Node(long value, long priority) {
            this.value = value;
            this.sum = value;
            this.min = value;
            this.priority = priority;
        }
    }

    private record Split(Node left, Node right) {}

    private record RangeParts(Node left, Node middle, Node right) {}
}

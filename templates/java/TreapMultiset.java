/**
 * Randomized multiset ordered by long keys.
 *
 * <p>Duplicates are stored in one node. All indices used by kth are zero-based.
 * Expected time per operation is O(log n).
 */
public final class TreapMultiset {
    private Node root;
    private long randomState;

    public TreapMultiset() {
        this(System.nanoTime());
    }

    /** Deterministic seed is useful for stress tests. */
    public TreapMultiset(long seed) {
        randomState = seed;
    }

    public int size() {
        return size(root);
    }

    public boolean isEmpty() {
        return root == null;
    }

    public void add(long key) {
        Split lessAndRest = splitLess(root, key);
        Split equalAndGreater = splitLessOrEqual(lessAndRest.right, key);

        Node equal = equalAndGreater.left;
        if (equal == null) {
            equal = new Node(key, nextPriority());
        } else {
            equal.count++;
            pull(equal);
        }

        root = merge(lessAndRest.left, merge(equal, equalAndGreater.right));
    }

    /** Removes one occurrence and returns false when the key is absent. */
    public boolean removeOne(long key) {
        Split lessAndRest = splitLess(root, key);
        Split equalAndGreater = splitLessOrEqual(lessAndRest.right, key);

        Node equal = equalAndGreater.left;
        boolean removed = equal != null;
        if (equal != null) {
            if (equal.count == 1) {
                equal = merge(equal.left, equal.right);
            } else {
                equal.count--;
                pull(equal);
            }
        }

        root = merge(lessAndRest.left, merge(equal, equalAndGreater.right));
        return removed;
    }

    public boolean contains(long key) {
        return count(key) != 0;
    }

    public int count(long key) {
        Node node = root;
        while (node != null) {
            if (key == node.key) return node.count;
            node = key < node.key ? node.left : node.right;
        }
        return 0;
    }

    /** Returns the key at the zero-based position in sorted order. */
    public long kth(int index) {
        if (index < 0 || index >= size()) throw new IndexOutOfBoundsException(index);
        Node node = root;
        while (true) {
            int leftSize = size(node.left);
            if (index < leftSize) {
                node = node.left;
            } else if (index < leftSize + node.count) {
                return node.key;
            } else {
                index -= leftSize + node.count;
                node = node.right;
            }
        }
    }

    public int countLessThan(long key) {
        int result = 0;
        Node node = root;
        while (node != null) {
            if (node.key >= key) {
                node = node.left;
            } else {
                result += size(node.left) + node.count;
                node = node.right;
            }
        }
        return result;
    }

    private Split splitLess(Node node, long key) {
        if (node == null) return new Split(null, null);
        if (node.key < key) {
            Split split = splitLess(node.right, key);
            node.right = split.left;
            pull(node);
            return new Split(node, split.right);
        }
        Split split = splitLess(node.left, key);
        node.left = split.right;
        pull(node);
        return new Split(split.left, node);
    }

    private Split splitLessOrEqual(Node node, long key) {
        if (node == null) return new Split(null, null);
        if (node.key <= key) {
            Split split = splitLessOrEqual(node.right, key);
            node.right = split.left;
            pull(node);
            return new Split(node, split.right);
        }
        Split split = splitLessOrEqual(node.left, key);
        node.left = split.right;
        pull(node);
        return new Split(split.left, node);
    }

    /** All keys in left must be strictly smaller than all keys in right. */
    private Node merge(Node left, Node right) {
        if (left == null) return right;
        if (right == null) return left;
        if (Long.compareUnsigned(left.priority, right.priority) > 0) {
            left.right = merge(left.right, right);
            pull(left);
            return left;
        }
        right.left = merge(left, right.left);
        pull(right);
        return right;
    }

    private static int size(Node node) {
        return node == null ? 0 : node.size;
    }

    private static void pull(Node node) {
        node.size = size(node.left) + node.count + size(node.right);
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
        final long key;
        final long priority;
        int count = 1;
        int size = 1;
        Node left;
        Node right;

        Node(long key, long priority) {
            this.key = key;
            this.priority = priority;
        }
    }

    private record Split(Node left, Node right) {}
}

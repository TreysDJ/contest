/** Zero-indexed Fenwick tree. prefixSum(right) returns the sum on [0, right). */
public final class Fenwick {
    private final long[] tree;

    public Fenwick(int n) {
        tree = new long[n + 1];
    }

    public void add(int index, long delta) {
        for (int i = index + 1; i < tree.length; i += i & -i) tree[i] += delta;
    }

    public long prefixSum(int right) {
        long result = 0;
        for (int i = right; i > 0; i -= i & -i) result += tree[i];
        return result;
    }

    public long rangeSum(int left, int right) {
        return prefixSum(right) - prefixSum(left);
    }

    /** Smallest zero-indexed p with prefixSum(p + 1) >= target; target must be positive. */
    public int lowerBound(long target) {
        int index = 0;
        int step = Integer.highestOneBit(tree.length - 1);
        for (; step != 0; step >>= 1) {
            int next = index + step;
            if (next < tree.length && tree[next] < target) {
                index = next;
                target -= tree[next];
            }
        }
        return index;
    }
}

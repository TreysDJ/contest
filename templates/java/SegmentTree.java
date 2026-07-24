/** Iterative segment tree for range sums on half-open intervals. */
public final class SegmentTree {
    private final int size;
    private final long[] tree;

    public SegmentTree(long[] values) {
        int s = 1;
        while (s < values.length) s <<= 1;
        size = s;
        tree = new long[size << 1];
        System.arraycopy(values, 0, tree, size, values.length);
        for (int i = size - 1; i > 0; i--) {
            tree[i] = tree[i << 1] + tree[i << 1 | 1];
        }
    }

    public void set(int index, long value) {
        int p = index + size;
        tree[p] = value;
        for (p >>= 1; p > 0; p >>= 1) {
            tree[p] = tree[p << 1] + tree[p << 1 | 1];
        }
    }

    public long query(int left, int right) {
        long resultLeft = 0;
        long resultRight = 0;
        for (left += size, right += size; left < right; left >>= 1, right >>= 1) {
            if ((left & 1) == 1) resultLeft += tree[left++];
            if ((right & 1) == 1) resultRight += tree[--right];
        }
        return resultLeft + resultRight;
    }
}

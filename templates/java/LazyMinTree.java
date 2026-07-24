/** Recursive lazy tree: add on [left, right), minimum on [left, right). */
public final class LazyMinTree {
    private final int n;
    private final long[] min;
    private final long[] lazy;

    public LazyMinTree(long[] values) {
        n = values.length;
        min = new long[Math.max(1, 4 * n)];
        lazy = new long[Math.max(1, 4 * n)];
        if (n > 0) build(1, 0, n, values);
    }

    private void build(int v, int left, int right, long[] values) {
        if (right - left == 1) {
            min[v] = values[left];
            return;
        }
        int mid = (left + right) >>> 1;
        build(v << 1, left, mid, values);
        build(v << 1 | 1, mid, right, values);
        pull(v);
    }

    private void apply(int v, long delta) {
        min[v] += delta;
        lazy[v] += delta;
    }

    private void push(int v) {
        if (lazy[v] != 0) {
            apply(v << 1, lazy[v]);
            apply(v << 1 | 1, lazy[v]);
            lazy[v] = 0;
        }
    }

    private void pull(int v) {
        min[v] = Math.min(min[v << 1], min[v << 1 | 1]);
    }

    public void add(int queryLeft, int queryRight, long delta) {
        add(1, 0, n, queryLeft, queryRight, delta);
    }

    private void add(int v, int left, int right, int ql, int qr, long delta) {
        if (qr <= left || right <= ql) return;
        if (ql <= left && right <= qr) {
            apply(v, delta);
            return;
        }
        push(v);
        int mid = (left + right) >>> 1;
        add(v << 1, left, mid, ql, qr, delta);
        add(v << 1 | 1, mid, right, ql, qr, delta);
        pull(v);
    }

    public long min(int queryLeft, int queryRight) {
        return min(1, 0, n, queryLeft, queryRight);
    }

    private long min(int v, int left, int right, int ql, int qr) {
        if (qr <= left || right <= ql) return Long.MAX_VALUE;
        if (ql <= left && right <= qr) return min[v];
        push(v);
        int mid = (left + right) >>> 1;
        return Math.min(
                min(v << 1, left, mid, ql, qr),
                min(v << 1 | 1, mid, right, ql, qr)
        );
    }
}

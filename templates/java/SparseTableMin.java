public final class SparseTableMin {
    private final int[] log;
    private final long[][] table;

    public SparseTableMin(long[] values) {
        int n = values.length;
        log = new int[n + 1];
        for (int i = 2; i <= n; i++) log[i] = log[i >> 1] + 1;
        table = new long[log[n] + 1][n];
        table[0] = values.clone();
        for (int k = 1; k < table.length; k++) {
            int length = 1 << k;
            for (int i = 0; i + length <= n; i++) {
                table[k][i] = Math.min(
                        table[k - 1][i],
                        table[k - 1][i + (length >> 1)]
                );
            }
        }
    }

    public long min(int left, int right) {
        int k = log[right - left];
        return Math.min(table[k][left], table[k][right - (1 << k)]);
    }
}

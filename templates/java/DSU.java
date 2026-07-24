public final class DSU {
    private final int[] parent;
    private final int[] size;
    private int components;

    public DSU(int n) {
        parent = new int[n];
        size = new int[n];
        components = n;
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
    }

    public int find(int v) {
        int root = v;
        while (root != parent[root]) root = parent[root];
        while (v != root) {
            int next = parent[v];
            parent[v] = root;
            v = next;
        }
        return root;
    }

    public boolean union(int a, int b) {
        a = find(a);
        b = find(b);
        if (a == b) return false;
        if (size[a] < size[b]) {
            int tmp = a;
            a = b;
            b = tmp;
        }
        parent[b] = a;
        size[a] += size[b];
        components--;
        return true;
    }

    public int componentSize(int v) {
        return size[find(v)];
    }

    public int components() {
        return components;
    }
}

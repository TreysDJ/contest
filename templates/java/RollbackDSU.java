import java.util.ArrayList;

/** Rollback DSU intentionally has no path compression. */
public final class RollbackDSU {
    private final int[] parent;
    private final int[] size;
    private final ArrayList<Change> history = new ArrayList<>();
    private int components;

    private record Change(int child, int parentRoot, int oldParentSize) {}

    public RollbackDSU(int n) {
        parent = new int[n];
        size = new int[n];
        components = n;
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
    }

    public int find(int v) {
        while (v != parent[v]) v = parent[v];
        return v;
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
        history.add(new Change(b, a, size[a]));
        parent[b] = a;
        size[a] += size[b];
        components--;
        return true;
    }

    public int snapshot() {
        return history.size();
    }

    public void rollback(int snapshot) {
        while (history.size() > snapshot) {
            Change change = history.remove(history.size() - 1);
            parent[change.child] = change.child;
            size[change.parentRoot] = change.oldParentSize;
            components++;
        }
    }

    public int components() {
        return components;
    }
}

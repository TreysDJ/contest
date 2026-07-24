import java.util.*;
import java.util.function.BiConsumer;

public final class TreeAlgorithms {
    private TreeAlgorithms() {}

    public static final class LCA {
        private final int[][] up;
        private final int[] depth;

        public LCA(List<Integer>[] tree, int root) {
            int n = tree.length;
            int log = 1;
            while ((1L << log) <= Math.max(1, n)) log++;
            up = new int[log][n];
            depth = new int[n];
            Arrays.fill(up[0], -1);

            int[] stack = new int[n];
            int size = 0;
            stack[size++] = root;
            up[0][root] = root;
            while (size > 0) {
                int v = stack[--size];
                for (int to : tree[v]) {
                    if (to == up[0][v]) continue;
                    up[0][to] = v;
                    depth[to] = depth[v] + 1;
                    stack[size++] = to;
                }
            }
            for (int k = 1; k < log; k++) {
                for (int v = 0; v < n; v++) up[k][v] = up[k - 1][up[k - 1][v]];
            }
        }

        public int kthAncestor(int v, int distance) {
            for (int bit = 0; bit < up.length; bit++) {
                if (((distance >>> bit) & 1) != 0) v = up[bit][v];
            }
            return v;
        }

        public int lca(int a, int b) {
            if (depth[a] < depth[b]) {
                int tmp = a;
                a = b;
                b = tmp;
            }
            a = kthAncestor(a, depth[a] - depth[b]);
            if (a == b) return a;
            for (int k = up.length - 1; k >= 0; k--) {
                if (up[k][a] != up[k][b]) {
                    a = up[k][a];
                    b = up[k][b];
                }
            }
            return up[0][a];
        }

        public int distance(int a, int b) {
            int c = lca(a, b);
            return depth[a] + depth[b] - 2 * depth[c];
        }

        public int depth(int v) { return depth[v]; }
    }

    /**
     * Iterative heavy-light decomposition. forEachPath emits inclusive position
     * segments; their direction is irrelevant for commutative operations.
     */
    public static final class HLD {
        public final int[] parent;
        public final int[] depth;
        public final int[] head;
        public final int[] position;
        public final int[] subtreeSize;
        private final List<Integer>[] tree;

        public HLD(List<Integer>[] tree, int root) {
            this.tree = tree;
            int n = tree.length;
            parent = new int[n];
            depth = new int[n];
            head = new int[n];
            position = new int[n];
            subtreeSize = new int[n];
            int[] heavy = new int[n];
            Arrays.fill(parent, -1);
            Arrays.fill(heavy, -1);

            int[] order = new int[n];
            int orderSize = 0;
            order[orderSize++] = root;
            for (int i = 0; i < orderSize; i++) {
                int v = order[i];
                for (int to : tree[v]) {
                    if (to == parent[v]) continue;
                    parent[to] = v;
                    depth[to] = depth[v] + 1;
                    order[orderSize++] = to;
                }
            }
            for (int i = n - 1; i >= 0; i--) {
                int v = order[i];
                subtreeSize[v] = 1;
                int bestSize = 0;
                for (int to : tree[v]) {
                    if (parent[to] != v) continue;
                    subtreeSize[v] += subtreeSize[to];
                    if (subtreeSize[to] > bestSize) {
                        bestSize = subtreeSize[to];
                        heavy[v] = to;
                    }
                }
            }

            int timer = 0;
            ArrayDeque<int[]> chains = new ArrayDeque<>();
            chains.push(new int[]{root, root});
            while (!chains.isEmpty()) {
                int[] chain = chains.pop();
                int start = chain[0];
                int chainHead = chain[1];
                for (int v = start; v != -1; v = heavy[v]) {
                    head[v] = chainHead;
                    position[v] = timer++;
                    for (int to : tree[v]) {
                        if (parent[to] == v && to != heavy[v]) chains.push(new int[]{to, to});
                    }
                }
            }
        }

        public void forEachPath(int a, int b, BiConsumer<Integer, Integer> consumer) {
            while (head[a] != head[b]) {
                if (depth[head[a]] < depth[head[b]]) {
                    int tmp = a;
                    a = b;
                    b = tmp;
                }
                consumer.accept(position[head[a]], position[a] + 1);
                a = parent[head[a]];
            }
            int left = Math.min(position[a], position[b]);
            int right = Math.max(position[a], position[b]);
            consumer.accept(left, right + 1);
        }
    }
}

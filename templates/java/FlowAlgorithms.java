import java.util.*;

public final class FlowAlgorithms {
    private FlowAlgorithms() {}

    public static final class Dinic {
        private static final long INF = Long.MAX_VALUE / 4;
        private final List<Edge>[] graph;
        private final int[] level;
        private final int[] pointer;

        private static final class Edge {
            int to;
            int reverse;
            long capacity;

            Edge(int to, int reverse, long capacity) {
                this.to = to;
                this.reverse = reverse;
                this.capacity = capacity;
            }
        }

        @SuppressWarnings("unchecked")
        public Dinic(int n) {
            graph = new ArrayList[n];
            for (int i = 0; i < n; i++) graph[i] = new ArrayList<>();
            level = new int[n];
            pointer = new int[n];
        }

        public void addEdge(int from, int to, long capacity) {
            Edge forward = new Edge(to, graph[to].size(), capacity);
            Edge backward = new Edge(from, graph[from].size(), 0);
            graph[from].add(forward);
            graph[to].add(backward);
        }

        private boolean bfs(int source, int sink) {
            Arrays.fill(level, -1);
            int[] queue = new int[graph.length];
            int head = 0;
            int tail = 0;
            level[source] = 0;
            queue[tail++] = source;
            while (head < tail) {
                int v = queue[head++];
                for (Edge edge : graph[v]) {
                    if (edge.capacity > 0 && level[edge.to] == -1) {
                        level[edge.to] = level[v] + 1;
                        queue[tail++] = edge.to;
                    }
                }
            }
            return level[sink] != -1;
        }

        private long dfs(int v, int sink, long pushed) {
            if (v == sink || pushed == 0) return pushed;
            for (; pointer[v] < graph[v].size(); pointer[v]++) {
                Edge edge = graph[v].get(pointer[v]);
                if (level[edge.to] != level[v] + 1 || edge.capacity == 0) continue;
                long flow = dfs(edge.to, sink, Math.min(pushed, edge.capacity));
                if (flow == 0) continue;
                edge.capacity -= flow;
                graph[edge.to].get(edge.reverse).capacity += flow;
                return flow;
            }
            return 0;
        }

        public long maxFlow(int source, int sink) {
            long result = 0;
            while (bfs(source, sink)) {
                Arrays.fill(pointer, 0);
                long pushed;
                while ((pushed = dfs(source, sink, INF)) > 0) result += pushed;
            }
            return result;
        }
    }

    /** Kuhn for a bipartite graph: left vertices [0, leftSize), right vertices [0, rightSize). */
    public static int[] kuhn(List<Integer>[] graph, int rightSize) {
        int[] matchedLeftByRight = new int[rightSize];
        Arrays.fill(matchedLeftByRight, -1);
        int[] seen = new int[graph.length];
        int iteration = 0;
        for (int left = 0; left < graph.length; left++) {
            iteration++;
            augment(left, graph, matchedLeftByRight, seen, iteration);
        }
        return matchedLeftByRight;
    }

    private static boolean augment(int left, List<Integer>[] graph, int[] match, int[] seen, int iteration) {
        if (seen[left] == iteration) return false;
        seen[left] = iteration;
        for (int right : graph[left]) {
            if (match[right] == -1 || augment(match[right], graph, match, seen, iteration)) {
                match[right] = left;
                return true;
            }
        }
        return false;
    }
}

import java.util.*;

public final class GraphAlgorithms {
    public static final long INF = Long.MAX_VALUE / 4;

    private GraphAlgorithms() {}

    public record Edge(int to, long weight) {}
    public record WeightedEdge(int from, int to, long weight) {}

    public static int[] bfs(List<Integer>[] graph, int source) {
        int[] distance = new int[graph.length];
        Arrays.fill(distance, -1);
        int[] queue = new int[graph.length];
        int head = 0;
        int tail = 0;
        distance[source] = 0;
        queue[tail++] = source;
        while (head < tail) {
            int v = queue[head++];
            for (int to : graph[v]) {
                if (distance[to] != -1) continue;
                distance[to] = distance[v] + 1;
                queue[tail++] = to;
            }
        }
        return distance;
    }

    public static long[] dijkstra(List<Edge>[] graph, int source) {
        long[] distance = new long[graph.length];
        Arrays.fill(distance, INF);
        PriorityQueue<State> queue = new PriorityQueue<>(Comparator.comparingLong(State::distance));
        distance[source] = 0;
        queue.add(new State(source, 0));
        while (!queue.isEmpty()) {
            State current = queue.poll();
            if (current.distance != distance[current.vertex]) continue;
            for (Edge edge : graph[current.vertex]) {
                long candidate = current.distance + edge.weight;
                if (candidate < distance[edge.to]) {
                    distance[edge.to] = candidate;
                    queue.add(new State(edge.to, candidate));
                }
            }
        }
        return distance;
    }

    private record State(int vertex, long distance) {}

    /** Edges must have weight 0 or 1. */
    public static long[] zeroOneBfs(List<Edge>[] graph, int source) {
        long[] distance = new long[graph.length];
        Arrays.fill(distance, INF);
        ArrayDeque<Integer> deque = new ArrayDeque<>();
        distance[source] = 0;
        deque.add(source);
        while (!deque.isEmpty()) {
            int v = deque.pollFirst();
            for (Edge edge : graph[v]) {
                if (edge.weight != 0 && edge.weight != 1) throw new IllegalArgumentException("weight must be 0 or 1");
                long candidate = distance[v] + edge.weight;
                if (candidate >= distance[edge.to]) continue;
                distance[edge.to] = candidate;
                if (edge.weight == 0) deque.addFirst(edge.to);
                else deque.addLast(edge.to);
            }
        }
        return distance;
    }

    /** Returns null if a reachable negative cycle exists. */
    public static long[] bellmanFord(int n, List<WeightedEdge> edges, int source) {
        long[] distance = new long[n];
        Arrays.fill(distance, INF);
        distance[source] = 0;
        for (int phase = 0; phase < n; phase++) {
            boolean changed = false;
            for (WeightedEdge edge : edges) {
                if (distance[edge.from] == INF) continue;
                long candidate = Math.max(-INF, distance[edge.from] + edge.weight);
                if (candidate < distance[edge.to]) {
                    distance[edge.to] = candidate;
                    changed = true;
                    if (phase == n - 1) return null;
                }
            }
            if (!changed) break;
        }
        return distance;
    }

    public static void floydWarshall(long[][] distance) {
        int n = distance.length;
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                if (distance[i][k] >= INF) continue;
                for (int j = 0; j < n; j++) {
                    if (distance[k][j] >= INF) continue;
                    distance[i][j] = Math.min(distance[i][j], distance[i][k] + distance[k][j]);
                }
            }
        }
    }

    /** Iterative Kosaraju; result components are numbered in topological order. */
    public static int[] stronglyConnectedComponents(List<Integer>[] graph, List<Integer>[] reverse) {
        int n = graph.length;
        boolean[] used = new boolean[n];
        int[] order = new int[n];
        int orderSize = 0;
        int[] nextEdge = new int[n];
        ArrayDeque<Integer> stack = new ArrayDeque<>();
        for (int start = 0; start < n; start++) {
            if (used[start]) continue;
            stack.push(start);
            used[start] = true;
            while (!stack.isEmpty()) {
                int v = stack.peek();
                if (nextEdge[v] < graph[v].size()) {
                    int to = graph[v].get(nextEdge[v]++);
                    if (!used[to]) {
                        used[to] = true;
                        stack.push(to);
                    }
                } else {
                    stack.pop();
                    order[orderSize++] = v;
                }
            }
        }

        int[] component = new int[n];
        Arrays.fill(component, -1);
        int count = 0;
        for (int i = n - 1; i >= 0; i--) {
            int start = order[i];
            if (component[start] != -1) continue;
            component[start] = count;
            stack.push(start);
            while (!stack.isEmpty()) {
                int v = stack.pop();
                for (int to : reverse[v]) {
                    if (component[to] == -1) {
                        component[to] = count;
                        stack.push(to);
                    }
                }
            }
            count++;
        }
        return component;
    }

    public static long kruskal(int n, List<WeightedEdge> edges) {
        ArrayList<WeightedEdge> sorted = new ArrayList<>(edges);
        sorted.sort(Comparator.comparingLong(WeightedEdge::weight));
        DSU dsu = new DSU(n);
        long result = 0;
        int taken = 0;
        for (WeightedEdge edge : sorted) {
            if (!dsu.union(edge.from, edge.to)) continue;
            result += edge.weight;
            taken++;
        }
        return taken == n - 1 ? result : INF;
    }

    /** Iterative low-link for an undirected multigraph. */
    public static LowLinkResult lowLink(int n, int[] from, int[] to) {
        if (from.length != to.length) throw new IllegalArgumentException("edge arrays differ");
        @SuppressWarnings("unchecked")
        List<IndexedEdge>[] graph = new ArrayList[n];
        for (int i = 0; i < n; i++) graph[i] = new ArrayList<>();
        for (int id = 0; id < from.length; id++) {
            graph[from[id]].add(new IndexedEdge(to[id], id));
            graph[to[id]].add(new IndexedEdge(from[id], id));
        }

        int[] tin = new int[n];
        int[] low = new int[n];
        int[] parent = new int[n];
        int[] parentEdge = new int[n];
        int[] nextEdge = new int[n];
        int[] children = new int[n];
        boolean[] bridge = new boolean[from.length];
        boolean[] articulation = new boolean[n];
        Arrays.fill(tin, -1);
        Arrays.fill(parent, -1);
        Arrays.fill(parentEdge, -1);
        int timer = 0;
        ArrayDeque<Integer> stack = new ArrayDeque<>();

        for (int root = 0; root < n; root++) {
            if (tin[root] != -1) continue;
            tin[root] = low[root] = timer++;
            stack.push(root);
            while (!stack.isEmpty()) {
                int v = stack.peek();
                if (nextEdge[v] < graph[v].size()) {
                    IndexedEdge edge = graph[v].get(nextEdge[v]++);
                    if (edge.id == parentEdge[v]) continue;
                    if (tin[edge.to] == -1) {
                        parent[edge.to] = v;
                        parentEdge[edge.to] = edge.id;
                        children[v]++;
                        tin[edge.to] = low[edge.to] = timer++;
                        stack.push(edge.to);
                    } else {
                        low[v] = Math.min(low[v], tin[edge.to]);
                    }
                } else {
                    stack.pop();
                    int p = parent[v];
                    if (p == -1) {
                        articulation[v] = children[v] > 1;
                    } else {
                        if (low[v] > tin[p]) bridge[parentEdge[v]] = true;
                        if (parent[p] != -1 && low[v] >= tin[p]) articulation[p] = true;
                        low[p] = Math.min(low[p], low[v]);
                    }
                }
            }
        }
        return new LowLinkResult(bridge, articulation);
    }

    private record IndexedEdge(int to, int id) {}
    public record LowLinkResult(boolean[] isBridge, boolean[] isArticulation) {}
}

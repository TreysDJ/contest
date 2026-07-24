import java.io.*;
import java.util.*;

public final class TemplateSelfTest {
    private static void check(boolean condition) {
        if (!condition) throw new AssertionError();
    }

    @SuppressWarnings("unchecked")
    public static void main(String[] args) throws Exception {
        FastScanner scanner = new FastScanner(new ByteArrayInputStream("-7 42 word".getBytes()));
        check(scanner.nextInt() == -7 && scanner.nextLong() == 42 && scanner.next().equals("word"));

        DSU dsu = new DSU(4);
        check(dsu.union(0, 1) && dsu.union(2, 3) && dsu.union(1, 2));
        check(dsu.components() == 1 && dsu.componentSize(3) == 4);

        RollbackDSU rollback = new RollbackDSU(3);
        int snapshot = rollback.snapshot();
        rollback.union(0, 1);
        rollback.union(1, 2);
        check(rollback.components() == 1);
        rollback.rollback(snapshot);
        check(rollback.components() == 3);

        Fenwick fenwick = new Fenwick(5);
        for (int i = 0; i < 5; i++) fenwick.add(i, i + 1);
        check(fenwick.prefixSum(5) == 15 && fenwick.rangeSum(1, 4) == 9);
        check(fenwick.lowerBound(7) == 3);

        SegmentTree segment = new SegmentTree(new long[]{1, 2, 3, 4});
        check(segment.query(1, 4) == 9);
        segment.set(2, 10);
        check(segment.query(0, 4) == 17);

        LazyMinTree lazy = new LazyMinTree(new long[]{5, 2, 7, 4});
        lazy.add(1, 3, 5);
        check(lazy.min(0, 4) == 4 && lazy.min(1, 3) == 7);
        SparseTableMin sparse = new SparseTableMin(new long[]{5, 2, 7, 4});
        check(sparse.min(1, 4) == 2);

        List<Integer>[] graph = new ArrayList[4];
        for (int i = 0; i < graph.length; i++) graph[i] = new ArrayList<>();
        addUndirected(graph, 0, 1);
        addUndirected(graph, 1, 2);
        addUndirected(graph, 1, 3);
        check(Arrays.equals(GraphAlgorithms.bfs(graph, 0), new int[]{0, 1, 2, 2}));

        List<GraphAlgorithms.Edge>[] weighted = new ArrayList[3];
        for (int i = 0; i < weighted.length; i++) weighted[i] = new ArrayList<>();
        weighted[0].add(new GraphAlgorithms.Edge(1, 5));
        weighted[0].add(new GraphAlgorithms.Edge(2, 20));
        weighted[1].add(new GraphAlgorithms.Edge(2, 4));
        check(GraphAlgorithms.dijkstra(weighted, 0)[2] == 9);
        check(GraphAlgorithms.kruskal(3, List.of(
                new GraphAlgorithms.WeightedEdge(0, 1, 2),
                new GraphAlgorithms.WeightedEdge(1, 2, 3),
                new GraphAlgorithms.WeightedEdge(0, 2, 10))) == 5);
        GraphAlgorithms.LowLinkResult lowLink = GraphAlgorithms.lowLink(
                4, new int[]{0, 1, 2, 1}, new int[]{1, 2, 0, 3});
        check(!lowLink.isBridge()[0] && !lowLink.isBridge()[1] && !lowLink.isBridge()[2]);
        check(lowLink.isBridge()[3] && lowLink.isArticulation()[1]);

        TreeAlgorithms.LCA lca = new TreeAlgorithms.LCA(graph, 0);
        check(lca.lca(2, 3) == 1 && lca.distance(2, 3) == 2);
        TreeAlgorithms.HLD hld = new TreeAlgorithms.HLD(graph, 0);
        boolean[] covered = new boolean[4];
        hld.forEachPath(2, 3, (left, right) -> {
            for (int i = left; i < right; i++) covered[i] = true;
        });
        check(count(covered) == 3);

        FlowAlgorithms.Dinic dinic = new FlowAlgorithms.Dinic(4);
        dinic.addEdge(0, 1, 2);
        dinic.addEdge(0, 2, 1);
        dinic.addEdge(1, 3, 2);
        dinic.addEdge(2, 3, 1);
        check(dinic.maxFlow(0, 3) == 3);

        List<Integer>[] bipartite = new ArrayList[2];
        bipartite[0] = new ArrayList<>(List.of(0, 1));
        bipartite[1] = new ArrayList<>(List.of(0));
        int[] matching = FlowAlgorithms.kuhn(bipartite, 2);
        check(matching[0] != -1 && matching[1] != -1);

        check(Arrays.equals(StringAlgorithms.prefixFunction("ababa"), new int[]{0, 0, 1, 2, 3}));
        check(Arrays.equals(StringAlgorithms.zFunction("aaaa"), new int[]{0, 3, 2, 1}));
        check(StringAlgorithms.manacher("abacaba")[0][3] == 4);
        StringAlgorithms.RollingHash hash = new StringAlgorithms.RollingHash("abcabc", 911382323L, 1_000_000_007L);
        check(hash.hash(0, 3) == hash.hash(3, 6));
        StringAlgorithms.AhoCorasick aho = new StringAlgorithms.AhoCorasick();
        aho.add("he");
        aho.add("she");
        aho.build();
        check(aho.countMatches("she") == 2);

        Geometry.Point a = new Geometry.Point(0, 0);
        Geometry.Point b = new Geometry.Point(2, 0);
        Geometry.Point c = new Geometry.Point(1, -1);
        Geometry.Point d = new Geometry.Point(1, 1);
        check(Geometry.segmentsIntersect(a, b, c, d));
        check(Geometry.signedDoubleArea(List.of(a, b, d)) == 2);
        check(Geometry.convexHull(List.of(a, b, c, d)).size() == 4);

        check(ModMath.gcd(42, 30) == 6 && ModMath.powMod(2, 10, 1_000_000_007) == 1024);
        check(ModMath.inverse(3, 11) == 4 && ModMath.factorize(60).equals(Map.of(2L, 2, 3L, 1, 5L, 1)));
        System.out.println("TemplateSelfTest: OK");
    }

    private static void addUndirected(List<Integer>[] graph, int a, int b) {
        graph[a].add(b);
        graph[b].add(a);
    }

    private static int count(boolean[] values) {
        int result = 0;
        for (boolean value : values) if (value) result++;
        return result;
    }
}

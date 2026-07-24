import java.util.*;

public final class StringAlgorithms {
    private StringAlgorithms() {}

    public static int[] prefixFunction(String text) {
        int[] pi = new int[text.length()];
        for (int i = 1; i < text.length(); i++) {
            int j = pi[i - 1];
            while (j > 0 && text.charAt(i) != text.charAt(j)) j = pi[j - 1];
            if (text.charAt(i) == text.charAt(j)) j++;
            pi[i] = j;
        }
        return pi;
    }

    public static int[] zFunction(String text) {
        int n = text.length();
        int[] z = new int[n];
        for (int i = 1, left = 0, right = 0; i < n; i++) {
            if (i < right) z[i] = Math.min(right - i, z[i - left]);
            while (i + z[i] < n && text.charAt(z[i]) == text.charAt(i + z[i])) z[i]++;
            if (i + z[i] > right) {
                left = i;
                right = i + z[i];
            }
        }
        return z;
    }

    /** d1[i] is the number of odd palindrome radii; d2[i] is the even radius ending before i. */
    public static int[][] manacher(String text) {
        int n = text.length();
        int[] d1 = new int[n];
        for (int i = 0, left = 0, right = -1; i < n; i++) {
            int k = i > right ? 1 : Math.min(d1[left + right - i], right - i + 1);
            while (i - k >= 0 && i + k < n && text.charAt(i - k) == text.charAt(i + k)) k++;
            d1[i] = k--;
            if (i + k > right) {
                left = i - k;
                right = i + k;
            }
        }
        int[] d2 = new int[n];
        for (int i = 0, left = 0, right = -1; i < n; i++) {
            int k = i > right ? 0 : Math.min(d2[left + right - i + 1], right - i + 1);
            while (i - k - 1 >= 0 && i + k < n && text.charAt(i - k - 1) == text.charAt(i + k)) k++;
            d2[i] = k--;
            if (i + k > right) {
                left = i - k - 1;
                right = i + k;
            }
        }
        return new int[][]{d1, d2};
    }

    public static final class RollingHash {
        private final long mod;
        private final long[] prefix;
        private final long[] power;

        public RollingHash(String text, long base, long mod) {
            this.mod = mod;
            prefix = new long[text.length() + 1];
            power = new long[text.length() + 1];
            power[0] = 1;
            for (int i = 0; i < text.length(); i++) {
                prefix[i + 1] = (prefix[i] * base + text.charAt(i)) % mod;
                power[i + 1] = power[i] * base % mod;
            }
        }

        public long hash(int left, int right) {
            long result = (prefix[right] - prefix[left] * power[right - left]) % mod;
            return result < 0 ? result + mod : result;
        }
    }

    /** Fixed lowercase alphabet; change ALPHABET/toIndex when a statement needs another alphabet. */
    public static final class AhoCorasick {
        private static final int ALPHABET = 26;
        private final ArrayList<Node> nodes = new ArrayList<>();

        private static final class Node {
            int[] next = new int[ALPHABET];
            int link;
            int outputCount;

            Node() { Arrays.fill(next, -1); }
        }

        public AhoCorasick() { nodes.add(new Node()); }

        public void add(String pattern) {
            int v = 0;
            for (int i = 0; i < pattern.length(); i++) {
                int c = pattern.charAt(i) - 'a';
                if (nodes.get(v).next[c] == -1) {
                    nodes.get(v).next[c] = nodes.size();
                    nodes.add(new Node());
                }
                v = nodes.get(v).next[c];
            }
            nodes.get(v).outputCount++;
        }

        public void build() {
            ArrayDeque<Integer> queue = new ArrayDeque<>();
            for (int c = 0; c < ALPHABET; c++) {
                int to = nodes.get(0).next[c];
                if (to == -1) nodes.get(0).next[c] = 0;
                else queue.add(to);
            }
            while (!queue.isEmpty()) {
                int v = queue.remove();
                Node node = nodes.get(v);
                node.outputCount += nodes.get(node.link).outputCount;
                for (int c = 0; c < ALPHABET; c++) {
                    int to = node.next[c];
                    if (to == -1) node.next[c] = nodes.get(node.link).next[c];
                    else {
                        nodes.get(to).link = nodes.get(node.link).next[c];
                        queue.add(to);
                    }
                }
            }
        }

        public int countMatches(String text) {
            int state = 0;
            int result = 0;
            for (int i = 0; i < text.length(); i++) {
                state = nodes.get(state).next[text.charAt(i) - 'a'];
                result += nodes.get(state).outputCount;
            }
            return result;
        }
    }
}

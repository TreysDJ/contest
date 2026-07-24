import java.util.*;

public final class ModMath {
    private ModMath() {}

    public static long gcd(long a, long b) {
        a = Math.abs(a);
        b = Math.abs(b);
        while (b != 0) {
            long remainder = a % b;
            a = b;
            b = remainder;
        }
        return a;
    }

    public static long lcm(long a, long b) {
        return a / gcd(a, b) * b;
    }

    public static long powMod(long base, long exponent, long mod) {
        base %= mod;
        long result = 1 % mod;
        while (exponent > 0) {
            if ((exponent & 1) != 0) result = result * base % mod;
            base = base * base % mod;
            exponent >>= 1;
        }
        return result;
    }

    /** Returns [g, x, y] with ax + by = g = gcd(a, b). */
    public static long[] extendedGcd(long a, long b) {
        long oldR = a, r = b;
        long oldX = 1, x = 0;
        long oldY = 0, y = 1;
        while (r != 0) {
            long quotient = oldR / r;
            long nextR = oldR - quotient * r;
            oldR = r;
            r = nextR;
            long nextX = oldX - quotient * x;
            oldX = x;
            x = nextX;
            long nextY = oldY - quotient * y;
            oldY = y;
            y = nextY;
        }
        return new long[]{oldR, oldX, oldY};
    }

    /** Modular inverse for any coprime value/modulus pair. */
    public static long inverse(long value, long mod) {
        long[] result = extendedGcd(value, mod);
        if (Math.abs(result[0]) != 1) throw new ArithmeticException("inverse does not exist");
        return Math.floorMod(result[1], mod);
    }

    public static int[] smallestPrimeFactor(int n) {
        int[] spf = new int[n + 1];
        for (int i = 0; i <= n; i++) spf[i] = i;
        if (n >= 1) spf[1] = 1;
        for (int i = 2; (long) i * i <= n; i++) {
            if (spf[i] != i) continue;
            for (int j = i * i; j <= n; j += i) {
                if (spf[j] == j) spf[j] = i;
            }
        }
        return spf;
    }

    public static Map<Long, Integer> factorize(long value) {
        LinkedHashMap<Long, Integer> factors = new LinkedHashMap<>();
        for (long divisor = 2; divisor <= value / divisor; divisor += divisor == 2 ? 1 : 2) {
            while (value % divisor == 0) {
                factors.merge(divisor, 1, Integer::sum);
                value /= divisor;
            }
        }
        if (value > 1) factors.put(value, 1);
        return factors;
    }
}

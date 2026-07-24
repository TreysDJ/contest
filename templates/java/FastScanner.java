import java.io.*;

/** Byte-based input for contest use. Keep the class package-private after copying into Main.java. */
public final class FastScanner {
    private static final int BUFFER_SIZE = 1 << 16;
    private final InputStream in;
    private final byte[] buffer = new byte[BUFFER_SIZE];
    private int pointer;
    private int length;

    public FastScanner(InputStream in) {
        this.in = in;
    }

    private int read() throws IOException {
        if (pointer >= length) {
            length = in.read(buffer);
            pointer = 0;
            if (length <= 0) return -1;
        }
        return buffer[pointer++];
    }

    public String next() throws IOException {
        StringBuilder result = new StringBuilder();
        int c;
        do {
            c = read();
        } while (c <= ' ' && c != -1);
        if (c == -1) return null;
        while (c > ' ') {
            result.append((char) c);
            c = read();
        }
        return result.toString();
    }

    public int nextInt() throws IOException {
        return Math.toIntExact(nextLong());
    }

    public long nextLong() throws IOException {
        int c;
        do {
            c = read();
        } while (c <= ' ' && c != -1);
        if (c == -1) throw new EOFException();
        int sign = 1;
        if (c == '-') {
            sign = -1;
            c = read();
        }
        long value = 0;
        while (c > ' ') {
            if (c < '0' || c > '9') throw new NumberFormatException();
            value = value * 10 + c - '0';
            c = read();
        }
        return sign * value;
    }
}

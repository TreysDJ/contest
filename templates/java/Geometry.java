import java.util.*;

public final class Geometry {
    private Geometry() {}

    public record Point(long x, long y) implements Comparable<Point> {
        @Override
        public int compareTo(Point other) {
            int byX = Long.compare(x, other.x);
            return byX != 0 ? byX : Long.compare(y, other.y);
        }
    }

    /** Beware of long overflow when coordinates or their differences approach 1e9 and beyond. */
    public static long cross(Point a, Point b, Point c) {
        return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x);
    }

    public static long dot(Point a, Point b, Point c) {
        return (b.x - a.x) * (c.x - a.x) + (b.y - a.y) * (c.y - a.y);
    }

    private static boolean between(long value, long left, long right) {
        return Math.min(left, right) <= value && value <= Math.max(left, right);
    }

    public static boolean onSegment(Point a, Point b, Point p) {
        return cross(a, b, p) == 0 && between(p.x, a.x, b.x) && between(p.y, a.y, b.y);
    }

    public static boolean segmentsIntersect(Point a, Point b, Point c, Point d) {
        long abC = cross(a, b, c);
        long abD = cross(a, b, d);
        long cdA = cross(c, d, a);
        long cdB = cross(c, d, b);
        if (abC == 0 && onSegment(a, b, c)) return true;
        if (abD == 0 && onSegment(a, b, d)) return true;
        if (cdA == 0 && onSegment(c, d, a)) return true;
        if (cdB == 0 && onSegment(c, d, b)) return true;
        return Long.signum(abC) != Long.signum(abD) && Long.signum(cdA) != Long.signum(cdB);
    }

    public static long signedDoubleArea(List<Point> polygon) {
        long result = 0;
        for (int i = 0; i < polygon.size(); i++) {
            Point a = polygon.get(i);
            Point b = polygon.get((i + 1) % polygon.size());
            result += a.x * b.y - a.y * b.x;
        }
        return result;
    }

    /** Returns unique hull vertices counterclockwise, without repeating the first point. */
    public static List<Point> convexHull(Collection<Point> input) {
        ArrayList<Point> points = new ArrayList<>(new TreeSet<>(input));
        if (points.size() <= 1) return points;
        ArrayList<Point> lower = new ArrayList<>();
        for (Point point : points) {
            while (lower.size() >= 2 && cross(lower.get(lower.size() - 2), lower.get(lower.size() - 1), point) <= 0) {
                lower.remove(lower.size() - 1);
            }
            lower.add(point);
        }
        ArrayList<Point> upper = new ArrayList<>();
        for (int i = points.size() - 1; i >= 0; i--) {
            Point point = points.get(i);
            while (upper.size() >= 2 && cross(upper.get(upper.size() - 2), upper.get(upper.size() - 1), point) <= 0) {
                upper.remove(upper.size() - 1);
            }
            upper.add(point);
        }
        lower.remove(lower.size() - 1);
        upper.remove(upper.size() - 1);
        lower.addAll(upper);
        return lower;
    }
}

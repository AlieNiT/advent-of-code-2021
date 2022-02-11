package code;

import java.math.BigInteger;

public class Main {
    static int[] dxs = new int[]{13, 15, 15, 11, -7, 10, 10, -5, 15, -3, 0, -5, -9, 0}; // add x < >
    static int[] dys = new int[]{6, 7, 10, 2, 15, 8, 1, 10, 5, 3, 5, 11, 12, 10};// add y < >
    static int[] bs = new int[]{0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1};// /1(0) or /26(1)

    public static void main(String[] args) {
        System.out.println(computeW(0, 0));
        printZ(computeW(0, 0));
    }
    private static void printZ(String W) {
        int z = 0;
        for (int i = 0; i < 14; i++) {
            z = next(z, W.charAt(i), dxs[i], dys[i], bs[i]);
            System.out.println(z);
        }
    }
    private static int next(int z, int w, int dx, int dy, int b) {
        if (((z % 26) + dx) == w) {
            return z / 26;
        }
        if (b == 0) {
            return w + dy + 26 * z;
        }
        return -1;
    }

    private static int nextW(int z, int dx) {
        int res = (z % 26) + dx;
        if (res < 1 | res > 9)
            return -1;
        return (z % 26) + dx;
    }

    private static String computeW(int z, int i) {
        int w;
        if (i == 14) {
            return "";
        }
        if (bs[i] == 1) {
            w = nextW(z, dxs[i]);
            if (w == -1)
                return null;
            z = next(z, w, dxs[i], dys[i], 1);
            if (z == -1)
                return null;
            String nextWs = computeW(z, i + 1);
            if (nextWs == null)
                return null;
            return w + nextWs;
        }
        BigInteger W = null;
        int tmp;
        for (int j = 1; j < 10; j++) {
            w = j;
            tmp = next(z, w, dxs[i], dys[i], 0);
            if (tmp == -1)
                continue;
            String nextWs = computeW(tmp, i + 1);
            if (nextWs == null)
                continue;
            if (W == null) {
                W = new BigInteger(j + nextWs);
            } else if (W.compareTo(new BigInteger(j + nextWs)) > 0) // part 1: <, part 2: >
                W = new BigInteger(j + nextWs);
        }
        if (W == null)
            return null;
        return W.toString();
    }
}
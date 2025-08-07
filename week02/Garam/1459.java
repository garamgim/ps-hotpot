import java.io.*;
import java.util.*;

public class 1459 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] info = br.readLine().split(" ");
        int X = Integer.parseInt(info[0]);
        int Y = Integer.parseInt(info[1]);
        int W = Integer.parseInt(info[2]);
        int S = Integer.parseInt(info[3]);

        long diff = Math.abs(X - Y);
        long square = min(X, Y);

        long diagonalCost = min(S * square, 2 * W * square);

        long remainingCost;

        if (diff == 0) {
            remainingCost = 0;
        } else if (diff % 2 == 0) {
            remainingCost = min(diff * W, diff * S);
        } else {
            remainingCost = min((diff - 1) * W, (diff - 1) * S) + W;
        }

        System.out.println(diagonalCost + remainingCost);
    }

    public static long min(long x, long y) {
        return (x < y) ? x : y;
    }
}

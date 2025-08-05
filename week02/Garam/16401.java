import java.io.*;
import java.util.*;

public class 16401 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] info = br.readLine().split(" ");
        int M = Integer.parseInt(info[0]);
        int N = Integer.parseInt(info[1]);

        String[] snackInfo = br.readLine().split(" ");
        int[] snacks = new int[N];

        int minSnack = Integer.MAX_VALUE;
        int maxSnack = 0;
        
        for (int i = 0; i < N; i++) {
            snacks[i] = Integer.parseInt(snackInfo[i]);

            if (minSnack > snacks[i]) {
                minSnack = snacks[i];
            }
            if (maxSnack < snacks[i]) {
                maxSnack = snacks[i];
            }
        }

        Arrays.sort(snacks);

        int l = 1;
        int r = maxSnack;
        
        int ans = 0;
        while (l <= r) {
            int mid = (l + r) / 2;
            
            int cnt = 0;
            for (int i = N - 1; i >= 0; i--) {
                int curr = snacks[i];
                int quotient = curr / mid;
                if (quotient == 0) break;
                cnt += quotient;
            }

            if (cnt >= M) {
                ans = mid;
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }

        System.out.println(ans);
    }
}

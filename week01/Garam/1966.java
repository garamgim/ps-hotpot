import java.io.*;
import java.util.*;

public class 1966 {
    static char[][] board;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int t = 0; t < T; t++) {
            String[] info = br.readLine().split(" ");
            int N = Integer.parseInt(info[0]);
            int M = Integer.parseInt(info[1]);

            String[] nums = br.readLine().split(" ");

            ArrayDeque<int[]> q = new ArrayDeque<>();
            PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());

            for (int i =     0; i < N; i++) {
                int num = Integer.parseInt(nums[i]);
                q.addLast(new int[]{num, i});
                pq.add(num);    
            }

            for (int i = 0; i < N; i++) {
                int[] curr = q.pollFirst();

                while (curr[0] < pq.peek()) {
                    q.add(curr);
                    curr = q.pollFirst();
                }

                pq.poll();
                if (curr[1] == M) {
                    System.out.println(i + 1);
                    break;
                }
            }
        }
        
    }
}

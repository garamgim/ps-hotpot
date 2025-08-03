import java.io.*;
import java.util.*;

public class 2468 {
    static int N;
    static int[][] area;
    static int[][] wetArea;
    static int minHeight = 101;
    static int maxHeight = 0;
    static int[] dr = new int[]{-1, 1, 0, 0};
    static int[] dc = new int[]{0, 0, -1, 1};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        area = new int[N][N];
        for (int i = 0; i < N; i++) {
            String[] info = br.readLine().split(" ");
            for (int j = 0; j < N; j++) {
                area[i][j] = Integer.parseInt(info[j]);
                if (area[i][j] < minHeight) minHeight = area[i][j];
                if (area[i][j] > maxHeight) maxHeight = area[i][j];
            }
        }

        if (minHeight == maxHeight) {
            System.out.println(1);
        } else {
            int maxArea = 0;


            for (int r = minHeight; r < maxHeight; r++) {
                wetArea = new int[N][N];
                for (int i = 0; i < N; i++) {
                    for (int j = 0; j < N; j++) {
                        if (area[i][j] <= r) {
                            wetArea[i][j] = -1;
                        } else {
                            wetArea[i][j] = area[i][j];
                        }
                    }
                }

                int cnt = 0;

                for (int i = 0; i < N; i++) {
                    for (int j = 0; j < N; j++) {
                        if (wetArea[i][j] != -1) {
                            cnt++;
                            bfs(i, j);
                        }
                    }
                }

                if (cnt > maxArea) {
                    maxArea = cnt;
                }
            }

            System.out.println(maxArea);
        }
    }

    static void bfs(int r, int c) {
        ArrayDeque<int[]> q = new ArrayDeque<>();
        q.addLast(new int[]{r, c});
        wetArea[r][c] = -1;

        while (!q.isEmpty()) {
            int[] curr = q.poll();

            for (int d = 0; d < 4; d++) {
                int nr = curr[0] + dr[d];
                int nc = curr[1] + dc[d];

                if (0 <= nr && nr < N && 0 <= nc && nc < N && wetArea[nr][nc] != -1) {
                    q.addLast(new int[]{nr, nc});
                    wetArea[nr][nc] = -1;
                }
            }
        }
    }
}

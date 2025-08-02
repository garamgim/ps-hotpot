import java.io.*;
import java.util.*;

public class 1753 {
    static int V, E, S;
    static ArrayList<ArrayList<int[]>> adjl;
    static int[] dist;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] info = br.readLine().split(" ");
        
        V = Integer.parseInt(info[0]);
        E = Integer.parseInt(info[1]);
        S = Integer.parseInt(br.readLine());

        dist = new int[V + 1];

        Arrays.fill(dist, Integer.MAX_VALUE);

        adjl = new ArrayList<>(V + 1);
        for (int i = 0; i <= V; i++) {
            adjl.add(new ArrayList<int[]>());
        }

        for (int i = 0; i < E; i++) {
            String[] pathInfo = br.readLine().split(" ");
            int u = Integer.parseInt(pathInfo[0]);
            int v = Integer.parseInt(pathInfo[1]);
            int w = Integer.parseInt(pathInfo[2]);
            adjl.get(u).add(new int[]{w, v});
        }

        djk();

        for (int i = 1; i <= V; i++) {
            if (dist[i] == Integer.MAX_VALUE) {
                System.out.println("INF");
            } else {
                System.out.println(dist[i]);
            }
        }

    }

    static void djk() {
        PriorityQueue<int[]> pq = new PriorityQueue<>((o1, o2) -> {
            return o1[0] - o2[0];
        });

        dist[S] = 0;
        pq.offer(new int[]{0, S});

        while (!pq.isEmpty()) {
            int[] curr = pq.poll();

            ArrayList<int[]> connected = adjl.get(curr[1]);

            for (int[] node : connected) {
                int accumulated = dist[curr[1]] + node[0];
                if (accumulated < dist[node[1]]) {
                    dist[node[1]] = accumulated;
                    pq.add(new int[]{accumulated, node[1]});
                }
            }
        }
    }
}

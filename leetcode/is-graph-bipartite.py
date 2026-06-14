class Solution {

    public boolean isBipartite(int[][] graph) {

        int n = graph.length;

        int[] color = new int[n];
        Arrays.fill(color, -1);

        for (int i = 0; i < n; i++) {

            if (color[i] == -1) {

                if (!bfs(graph, color, i))
                    return false;
            }
        }

        return true;
    }

    boolean bfs(int[][] graph,
                int[] color,
                int start) {

        Queue<Integer> q = new LinkedList<>();

        q.offer(start);
        color[start] = 0;

        while (!q.isEmpty()) {

            int node = q.poll();

            for (int next : graph[node]) {

                if (color[next] == -1) {

                    color[next] = 1 - color[node];
                    q.offer(next);
                }

                else if (color[next] == color[node]) {

                    return false;
                }
            }
        }

        return true;
    }
}
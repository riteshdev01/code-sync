class Solution {
    class Triple {
        int node;
        int parent;
        int dist;

        Triple(int node, int parent, int dist) {
            this.node = node;
            this.parent = parent;
            this.dist = dist;
        }
    }

    public int minCostConnectPoints(int[][] points) {

        int n = points.length;

        PriorityQueue<Triple> pq =
                new PriorityQueue<>((a, b) -> a.dist - b.dist);

        boolean[] vis = new boolean[n];

        pq.add(new Triple(0, -1, 0));

        int sum = 0;

        while (!pq.isEmpty()) {

            Triple curr = pq.poll();

            int node = curr.node;
            int dist = curr.dist;

            if (vis[node])
                continue;

            vis[node] = true;
            sum += dist;

            for (int i = 0; i < n; i++) {

                if (!vis[i]) {

                    int cost =
                            Math.abs(points[node][0] - points[i][0]) +
                            Math.abs(points[node][1] - points[i][1]);

                    pq.add(new Triple(i, node, cost));
                }
            }
        }

        return sum;
    }
}
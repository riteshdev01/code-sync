class Solution {
    public int findTheCity(int n, int[][] edges, int distanceThreshold) {

        int[][] dist = new int[n][n];

        for (int[] x : dist) {
            Arrays.fill(x, Integer.MAX_VALUE);
        }

        for(int i = 0 ; i < n ;i++) dist[i][i] = 0;

        for (int[] a : edges) {
            int u = a[0];
            int v = a[1];
            int wt = a[2];

            dist[u][v] = wt;
            dist[v][u] = wt;
        }

        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {

                    if (dist[i][k] != Integer.MAX_VALUE && dist[k][j] != Integer.MAX_VALUE) {
                        dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
                    }

                }
            }
        }

        int mincity = -1;
        int mincount = 1000;

        for (int i = 0; i < n; i++) {
            int count = 0;
            for (int j = 0; j < n; j++) {
                if (i == n || j == n)
                    continue;

                if (dist[i][j] <= distanceThreshold) {
                    count++;
                }
            }

            if (count <= mincount) {
                mincity = i;
                mincount = count;
            }
        }

        return mincity;

    }
}
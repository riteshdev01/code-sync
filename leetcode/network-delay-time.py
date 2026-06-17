class Solution {
    class Pair {
        int node;
        int time;

        Pair(int node, int dist) {
            this.node = node;
            this.time = dist;
        }
    }

    public int networkDelayTime(int[][] times, int n, int k) {

        ArrayList<ArrayList<Pair>> adj = new ArrayList<>();

        for (int i = 0; i <= n; i++)
            adj.add(new ArrayList<Pair>());

        for (int i = 0; i < times.length; i++) {
            int a = times[i][0];
            int b = times[i][1];
            int time = times[i][2];

            adj.get(a).add(new Pair(b, time));
        }

        PriorityQueue<Pair> pq = new PriorityQueue<>((a, b) -> a.time - b.time);

        int[] ans = new int[n + 1];
        Arrays.fill(ans, Integer.MAX_VALUE);

        ans[k] = 0;

        pq.add(new Pair(k, 0));

        while (!pq.isEmpty()) {
            Pair p = pq.poll();
            int curr = p.node;
            int time = p.time;

            if (time > ans[curr])
                continue;

            for (Pair x : adj.get(curr)) {
                int totaltime = time + x.time;

                if (totaltime < ans[x.node]) {
                    ans[x.node] = totaltime;

                    pq.add(new Pair(x.node, totaltime));
                }
            }

        }

        int max = -1;
        for (int i = 1; i <= n; i++) {

            if (ans[i] == Integer.MAX_VALUE)
                return -1;

            max = Math.max(max, ans[i]);
        }

        return max;
    }
}
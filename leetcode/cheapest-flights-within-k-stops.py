class Solution {
    class Pair {
        int node;
        int cost;

        Pair(int node, int cost) {
            this.node = node;
            this.cost = cost;
        }
    }

    class Triplet {
        int node;
        int cost;
        int stop;

        Triplet(int node, int cost, int stop) {
            this.node = node;
            this.cost = cost;
            this.stop = stop;
        }
    }

    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {

        ArrayList<ArrayList<Pair>> adj = new ArrayList<>();

        for (int i = 0; i < n; i++)
            adj.add(new ArrayList<Pair>());

        for (int[] f : flights) {
            int u = f[0];
            int v = f[1];
            int x = f[2];

            adj.get(u).add(new Pair(v, x));
        }

        int[] ans = new int[n];
        Arrays.fill(ans, Integer.MAX_VALUE);

        ans[src] = 0;

        Queue<Triplet> q = new LinkedList<>();
        q.add(new Triplet(src, 0, 0));

        while (!q.isEmpty()) {
            Triplet t = q.poll();
            int node = t.node, c = t.cost;

            if (t.stop > k )
                continue;

            for (Pair p : adj.get(node)) {
                int totalcost = c + p.cost;

                

                if (totalcost < ans[p.node]) {
                    ans[p.node] = totalcost;
                    q.add(new Triplet(p.node, totalcost, t.stop + 1));
                }
            }
        }

        return ( ans[dst] == Integer.MAX_VALUE)  ?  -1 :  ans[dst];

    }
}
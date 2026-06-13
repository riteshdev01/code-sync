class Solution {

    public int findCircleNum(int[][] isConnected) {

        int n = isConnected.length;
        boolean[] visited = new boolean[n];

        int count = 0;

        for (int i = 0; i < n; i++) {

            if (!visited[i]) {
                count++;
                dfs(isConnected, visited, i);
            }

        }

        return count;
    }

    void bfs(int[][] isConnected,
            boolean[] visited,
            int city) {

        visited[city] = true;

        Queue <Integer> q = new LinkedList<>();

        q.add(city);

        while(!q.isEmpty()){
            int curr = q.poll();

            for(int j = 0 ;  j < isConnected.length ; j++){
                if( isConnected[curr][j] == 1 && visited[j] == false){
                    visited[j] = true;
                    q.add(j);
                }
            }
        }

    }
}
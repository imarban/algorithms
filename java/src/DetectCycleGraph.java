public class DetectCycleGraph {

    public static void main(String[] args) {
        int[][] matrix = {
                {0,0,0,1,1},
                {0,1,1,0,0},
                {0,0,1,1,0},
                {1,0,1,0,0},
                {1,1,0,0,0}
        };

        DetectCycleGraph detectCycleGraph = new DetectCycleGraph();

        System.out.println(detectCycleGraph.isCycle(matrix, 5, 5));
    }

    private boolean isCycle(int[][] matrix, int n, int m) {
        boolean [][] visited = new boolean[n][m];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                visited[i][j] = false;
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (!visited[i][j] && matrix[i][j] == 1) {
                    if(isCycleUtil(matrix, i, j, n, m, visited, new int[]{i, j})) {
                        return true;
                    }
                }
            }
        }

        return false;
    }

    private boolean canMove(int i, int j, int n, int m, int[][] matrix, boolean[][] visited) {
        boolean isInBound = i >= 0 && j >= 0 &&  i < n && j < m;
        return isInBound && matrix[i][j] == 1 && !visited[i][j];
    }

    private boolean isCycleUtil(int[][] matrix, int i, int j, int n, int m, boolean[][] visited, int[] parent) {

        visited[i][j] = true;
        int[] newParent = new int[]{i, j};
        //right
        if (moveTo(matrix, i, j + 1, n, m, visited, parent, newParent)) return true;
        //down
        if (moveTo(matrix, i + 1, j, n, m, visited, parent, newParent)) return true;
        //left
        if (moveTo(matrix, i, j - 1, n, m, visited, parent, newParent)) return true;
        //top
        if (moveTo(matrix, i - 1, j, n, m, visited, parent, newParent)) return true;

        return false;

    }

    private boolean moveTo(int[][] matrix, int i, int j, int n, int m, boolean[][] visited, int[] parent, int[] newParent) {
        if (canMove(i, j, n, m, matrix, visited)) {
            return isCycleUtil(matrix, i, j, n, m, visited, newParent);
        } else if (i>=0 && j>=0 && i<n && j<n) {
            return visited[i][j] && parent[0] != i && parent[1] != j;
        }
        return false;
    }

}

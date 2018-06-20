public class Islands {

    public static void main(String[] args) {

        int[][] matrix = {
                {1,0,0,1,1},
                {0,1,1,0,0},
                {0,0,1,1,0},
                {1,1,0,1,0},
                {1,1,0,0,0}
        };

        Islands islands = new Islands();
        System.out.println(islands.countObjects(matrix, 5, 5));

        int[][] matrix2 = {{0,0,0,1,1}, {0,0,0,0,0}, {0,0,1,1,0}, {0,0,0,0,0}, {1,1,0,0,0}};
        System.out.println(islands.countObjects(matrix2, 5, 5));

    }

    private int countObjects(int[][] matrix, int n, int m) {

        boolean[][] visited = new boolean[n][m];

        for (int i = 0; i < n ; i++) {
            for (int j = 0; j < m; j++) {
                visited[i][j] = false;
            }
        }

        int result = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (matrix[i][j] == 1 && !visited[i][j]) {
                    countObjectsUtil(matrix, visited, i, j, n, m);
                    result += 1;
                }
            }

        }

        return result;
    }

    private void countObjectsUtil(int[][] matrix, boolean[][] visited, int i, int j, int n, int m) {

        visited[i][j] = true;

        // right
        if (canMove(i, j+1, n, m, matrix, visited)) {
            countObjectsUtil(matrix, visited, i, j + 1, n, m);
        }

        // down
        if (canMove(i + 1, j, n, m, matrix, visited)) {
            countObjectsUtil(matrix, visited, i + 1, j, n, m);
        }

        // left
        if (canMove(i, j - 1, n, m, matrix, visited)) {
            countObjectsUtil(matrix, visited, i, j - 1, n, m);
        }

        // up
        if (canMove(i - 1, j, n, m, matrix, visited)) {
            countObjectsUtil(matrix, visited, i - 1, j, n, m);
        }

    }

    private boolean canMove(int i, int j, int n, int m, int[][] matrix, boolean[][] visited) {
        boolean isInBounds =  i >= 0 && j >= 0 && i < n && j < m;
        return isInBounds && matrix[i][j] ==  1 && !visited[i][j];
    }

}

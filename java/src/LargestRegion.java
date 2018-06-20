public class LargestRegion {

    public static void main(String[] args) {
        int[][] matrix = {
                {0,0,0,1,1},
                {0,1,1,0,0},
                {0,0,1,1,0},
                {1,1,0,1,0},
                {1,1,0,0,0}
        };

        LargestRegion largestRegion = new LargestRegion();
        largestRegion.getLengthLargestRegion(matrix, 5, 5);
    }

    private void getLengthLargestRegion(int[][] matrix, int n, int m) {
        boolean[][] visited = new boolean[n][m];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                visited[i][j] = false;
            }
        }

        int maxLength = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (matrix[i][j] == 1 && !visited[i][j]) {
                    int length = getLengthLargestRegionUtil(matrix, i, j, n, m, visited, 0);
                    if (length > maxLength) {
                        maxLength = length;
                    }
                }
            }
        }

        System.out.println(maxLength);

    }

    private boolean canMove(int i, int j, int n, int m, int[][] matrix, boolean[][] visited) {
        boolean isInBounds =  i >= 0 && j >= 0 && i < n && j < m;
        return isInBounds && matrix[i][j] ==  1 && !visited[i][j];
    }

    private int getLengthLargestRegionUtil(int[][] matrix, int i, int j, int n, int m, boolean[][] visited, int result) {

        visited[i][j] = true;
        result++;

        // right
        if (canMove(i, j+1, n, m, matrix, visited)) {
            result = getLengthLargestRegionUtil(matrix, i, j + 1, n, m, visited, result);
        }

        // down
        if (canMove(i + 1, j, n, m, matrix, visited)) {
            result = getLengthLargestRegionUtil(matrix, i + 1, j, n, m, visited, result);
        }

        // left
        if (canMove(i, j - 1, n, m, matrix, visited)) {
            result = getLengthLargestRegionUtil(matrix, i, j - 1, n, m, visited, result);
        }

        // up
        if (canMove(i - 1, j, n, m, matrix, visited)) {
            result = getLengthLargestRegionUtil(matrix, i - 1, j, n, m, visited, result);
        }

        return result;

    }

}

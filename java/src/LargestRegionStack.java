import java.util.Arrays;
import java.util.List;
import java.util.Stack;

public class LargestRegionStack {

    public static void main(String[] args) {
        int[][] matrix = {
                {0,0,0,1,1},
                {0,1,1,0,0},
                {0,0,0,1,0},
                {1,1,0,1,0},
                {1,0,0,0,0}
        };

        LargestRegionStack largestRegion = new LargestRegionStack();
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
                    int length = getLengthLargestRegionUtil(matrix, i, j, n, m, visited);
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

    private int getLengthLargestRegionUtil(int[][] matrix, int k, int l, int n, int m, boolean[][] visited) {

        Stack<List<Integer>> stack = new Stack<>();
        stack.push(Arrays.asList(k, l));
        int result = 0;

        while (!stack.isEmpty()) {
            List<Integer> indexes = stack.pop();
            int i = indexes.get(0);
            int j = indexes.get(1);

            if (!visited[i][j]) {
                visited[i][j] = true;
                result++;
            }

            // right
            if (canMove(i, j + 1, n, m, matrix, visited)) {
                stack.push(Arrays.asList(i, j + 1));
            }

            // down
            if (canMove(i + 1, j, n, m, matrix, visited)) {
                stack.push(Arrays.asList(i + 1, j));
            }

            // left
            if (canMove(i, j - 1, n, m, matrix, visited)) {
                stack.push(Arrays.asList(i, j - 1));
            }

            // up
            if (canMove(i - 1, j, n, m, matrix, visited)) {
                stack.push(Arrays.asList(i - 1, j));
            }

        }

        return result;
    }

}

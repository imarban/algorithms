import java.util.*;

public class Boggle {

    public static void main(String[] args) {
        Boggle boggle = new Boggle();

        List<Character> board = Arrays.asList('G', 'I', 'Z', 'U', 'E', 'K', 'Q', 'S', 'E');
        int n = 3;
        int m = 3;
        Set<String> dict = new HashSet<>(Arrays.asList("GEEKS", "FOR", "QUIZ", "GO"));

        boggle.findWords(board, n, m, dict);
    }

    private boolean isWord(String str, Set<String> dict) {
        return dict.contains(str);
    }

    private void findWordsUtil(List<Character> board, int n, int m, List<Boolean> visited,
                               int i, int j, StringBuffer str, Set<String> dict) {

        visited.set(i * m + j, true);
        str.append(board.get(i * m + j));

        if (isWord(str.toString(), dict)) {
            System.out.println(str.toString());
        }

        for (int row = i-1; row <= i+1 && row < n; row++) {
            for (int col = j-1; col <= j+1 && col < m; col++) {
                if (row >= 0 && col >= 0 && !visited.get(row * m + col)) {
                    findWordsUtil(board, n, m, visited, row, col, str,  dict);
                }
            }
        }

        str.deleteCharAt(str.length() - 1);
        visited.set(i * m + j, false);
    }

    private void findWords(List<Character> board, int n, int m, Set<String> dict) {
        List<Boolean> visited = new ArrayList<>();
        for (int i = 0; i < n * m; i++) {
            visited.add(false);
        }

        StringBuffer stringBuffer = new StringBuffer();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                findWordsUtil(board, n, m, visited, i, j, stringBuffer, dict);
            }
        }
    }
}

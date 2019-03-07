import java.util.StringJoiner;

/**
 * Created by igomez on 7/25/15.
 */
public class CompleteThePattern {
    public static String pattern(int n) {
        if (n < 1) {
            return "";
        }
        StringJoiner sb = new StringJoiner("\n");
        for (int i = 1; i <= n; i++) {
            sb.add(generatePattern(n, i));
        }

        return sb.toString();

    }


    public static String generatePattern(int top, int low) {
        StringBuilder sb = new StringBuilder();
        for (int i = top; i >= low; i--) {
            sb.append(String.valueOf(i));
        }
        return sb.toString();
    }
}

public class DigPow {

    public static long digPow(int n, int p) {
        int sum = 0;
        int reversed = reverse(n);
        int digit;

        while (reversed != 0) {
            digit = reversed % 10;
            sum += pow(digit, p++);
            reversed /= 10;
        }

        return getDivisor(sum, n);
    }

    public static int reverse(int n){
        int digit;
        String  strValue = "";
        while (n != 0) {
            digit = n % 10;
            strValue += String.valueOf(digit);
            n /= 10;
        }
        return Integer.parseInt(strValue);
    }

    public static int pow(int n, int p) {
        int result = n;
        for (int i = 2; i <= p; i++) {
            result *= n;
        }

        return result;
    }

    public static int getDivisor(int sum, int originalNumber) {
        float result = (float)sum/originalNumber;
        return 0 == result %1 ? (int) result : -1;
    }

}

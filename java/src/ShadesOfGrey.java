/**
 * Created by igomez on 7/25/15.
 */
public class ShadesOfGrey {
    static String[] shadesOfGrey(int num) {
        // returns n shades of grey in an array
        if (num < 1) {
            return new String[0];
        }

        String[] shades = new String[num <= 254 ? num : 254];

        for (int i = 1; i <= shades.length; i++) {
            shades[i-1] = String.format("#%06X", (i << 16) + (i << 8) + i).toLowerCase();
        }

        return shades;
    }
}

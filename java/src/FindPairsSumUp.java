import java.util.*;
import java.util.stream.Collectors;

public class FindPairsSumUp {

    public static void main(String... args) {

        FindPairsSumUp findPairsSumUp = new FindPairsSumUp();
        Integer[] test1 = {3, 4, 1, 5, 7, 2, 10};
        Integer[] test2 = {0, 6, 4, 10, 9, 1};

        List<Map.Entry<Integer,  Integer>> pairs1 = findPairsSumUp.getUniquePairs(Arrays.asList(test1), 12 );
        List<Map.Entry<Integer,  Integer>> pairs2 = findPairsSumUp.getUniquePairs(Arrays.asList(test2), 10 );

        System.out.println(pairs1.stream().map(n-> "(" + n.getKey().toString() + "," + n.getValue() + ")").collect(Collectors.joining(", ")));
        System.out.println(pairs2.stream().map(n-> "(" + n.getKey().toString() + "," + n.getValue() + ")").collect(Collectors.joining(", ")));

    }

    private List<Map.Entry<Integer,Integer>> getPairs(List<Integer> values, Integer target) {
        Map<Integer, Integer> frequencies = new HashMap<>();
        List<Map.Entry<Integer,Integer>> results = new ArrayList<>();

        for (Integer value:values) {
            int currentCount = frequencies.getOrDefault(value, 0);
            frequencies.put(value, currentCount + 1);
        }

        for (Integer value:values) {
            int lookingFor = target - value;
            if (frequencies.containsKey(lookingFor) && frequencies.get(lookingFor) > 0) {
                results.add(new AbstractMap.SimpleEntry<>(lookingFor, value));
                int currentCount = frequencies.get(lookingFor);
                frequencies.put(lookingFor, currentCount - 1);
            }
        }

        return results;

    }

    private List<Map.Entry<Integer,Integer>> getUniquePairs(List<Integer> values, Integer target) {
        Map<Integer, Integer> frequencies = new HashMap<>();
        List<Map.Entry<Integer,Integer>> results = new ArrayList<>();

        for (Integer value:values) {
            int lookingFor = target - value;
            if (frequencies.containsKey(lookingFor) && frequencies.get(lookingFor) > 0) {
                results.add(new AbstractMap.SimpleEntry<>(lookingFor, value));
                int currentCount = frequencies.get(lookingFor);
                frequencies.put(lookingFor, currentCount - 1);
            } else {
                frequencies.put(value, 1);
            }
        }

        return results;
    }


}

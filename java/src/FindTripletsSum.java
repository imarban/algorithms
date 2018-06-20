import java.util.*;
import java.util.stream.Collectors;

public class FindTripletsSum {

    public static void main(String... args) {
        FindTripletsSum findTripletsSum = new FindTripletsSum();

        List<List<Integer>> triplets = findTripletsSum.getTriplets(
                Arrays.asList(3, 4, 1, 5, 7, 2, 10, 0, 0), 12 );

        List<List<Integer>> triplets2 = findTripletsSum.getTriplets(
                Arrays.asList(0, 3, 1, 5, 1, 2, 0), 5 );

        findTripletsSum.printResults(triplets);
        findTripletsSum.printResults(triplets2);

    }

    private void printResults(List<List<Integer>> results) {
        System.out.println(results.stream().map(triplet -> "(" +
            triplet.stream().map(Object::toString).collect(
                    Collectors.joining(",")) + ")").collect(Collectors.joining(", ")));
    }

    private List<List<Integer>> getTriplets(List<Integer> values, int target) {
        List<List<Integer>> results = new ArrayList<>();
        Collections.sort(values);
        for (int i = 0; i < values.size() - 2; i++) {
            int leftIndex = i + 1;
            int rightIndex = values.size() - 1;
            while(leftIndex < rightIndex) {
                int currentSum = values.get(i) + values.get(leftIndex) + values.get(rightIndex);
                if (currentSum > target) {
                    rightIndex -= 1;
                }
                else if (currentSum < target) {
                    leftIndex += 1;
                }
                else {
                    List<Integer> triplet = new ArrayList<>();
                    triplet.add(values.get(i));
                    triplet.add(values.get(leftIndex));
                    triplet.add(values.get(rightIndex));

                    results.add(triplet);
                    rightIndex -= 1;
                    leftIndex += 1;
                }
            }
        }

        return results;
    }

    private List<List<Integer>> getUniqueTriplets(List<Integer> values, int target) {
        Set<String> unique = new HashSet<>();
        List<List<Integer>> triplets = getTriplets(values, target);
        List<List<Integer>> uniqueTriplets = new ArrayList<>();

        triplets.forEach(
                triplet-> {
                    String tripletString =
                            triplet.stream().map(Object::toString).collect(Collectors.joining(","));
                    boolean added = unique.add(tripletString);
                    if (added) {
                        uniqueTriplets.add(triplet);
                    }
                });

        return uniqueTriplets;
    }

}

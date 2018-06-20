import java.util.*;
import java.util.stream.Collectors;

public class FindFourSumUp {

    public static void main(String[] args) {
        FindFourSumUp findFourSumUp = new FindFourSumUp();

        List<List<Integer>> results = findFourSumUp.findFour(Arrays.asList(10, 2, 3, 4, 5, 9, 7, 8), 23 );
        findFourSumUp.printResults(results);
        List<List<Integer>> resultsSort = findFourSumUp.findFourUsingSort(Arrays.asList(10, 2, 3, 4, 5, 9, 7, 8), 23 );
        findFourSumUp.printResults(resultsSort);

    }

    private void printResults(List<List<Integer>> results) {
        System.out.println(results.stream().map(triplet -> "(" +
                triplet.stream().map(Object::toString).collect(
                        Collectors.joining(",")) + ")").collect(Collectors.joining(", ")));
    }

    private List<List<Integer>> findFour(List<Integer> values, int target) {

        Map<Integer, List<Integer>> partialSums = new HashMap<>();
        Set<List<Integer>> results = new HashSet<>();

        for (int i = 0; i < values.size(); i++) {
            for (int j = i + 1; j < values.size(); j++) {
                partialSums.put(values.get(i) + values.get(j), Arrays.asList(i, j));
            }
        }

        for (int i = 0; i < values.size() - 1; i++) {
            for (int j = i + 1; j < values.size(); j++) {
                int sum = values.get(i) + values.get(j);
                int lookingFor = target - sum;
                if (partialSums.containsKey(lookingFor)) {
                    List<Integer> pairFound = partialSums.get(lookingFor);
                    if(noCommonIndices(pairFound, i, j)) {
                        List<Integer> toAdd = Arrays.asList(values.get(pairFound.get(0)), values.get(pairFound.get(1)),
                                values.get(i), values.get(j));
                        Collections.sort(toAdd);
                        results.add(toAdd);
                    }
                }
            }
        }

        return new ArrayList<>(results);

    }

    private boolean noCommonIndices(List<Integer> pair, int i, int j) {
        return pair.get(0) != i && pair.get(0) != j &&
                pair.get(1) != i && pair.get(1) != j;
    }

    private boolean noCommonIndices(List<Integer> pair1, List<Integer> pair2) {
        return !pair1.get(0).equals(pair2.get(0)) && !pair1.get(0).equals(pair2.get(1)) &&
                !pair1.get(1).equals(pair2.get(0)) && !pair1.get(1).equals(pair2.get(1));
    }


    private List<List<Integer>> findFourUsingSort(List<Integer> values, int target) {

        List<Map.Entry<Integer, List<Integer>>> partialSums = new ArrayList<>();
        Set<List<Integer>> results = new HashSet<>();

        for (int i = 0; i < values.size(); i++) {
            for (int j = i + 1; j < values.size(); j++) {
                partialSums.add(new AbstractMap.SimpleEntry<>(values.get(i) + values.get(j), Arrays.asList(i, j)));
            }
        }

        partialSums.sort(Comparator.comparingInt(Map.Entry::getKey));

        int leftIndex = 0;
        int rightIndex = partialSums.size() - 1;

        while(leftIndex < partialSums.size() && rightIndex >= 0) {
            int currentSum = partialSums.get(leftIndex).getKey() + partialSums.get(rightIndex).getKey();
            if (currentSum == target &&
                    noCommonIndices(partialSums.get(leftIndex).getValue(), partialSums.get(rightIndex).getValue())) {
                List<Integer> fourNumbers = new ArrayList<>();
                fourNumbers.add(values.get(partialSums.get(leftIndex).getValue().get(0)));
                fourNumbers.add(values.get(partialSums.get(leftIndex).getValue().get(1)));
                fourNumbers.add(values.get(partialSums.get(rightIndex).getValue().get(0)));
                fourNumbers.add(values.get(partialSums.get(rightIndex).getValue().get(1)));
                Collections.sort(fourNumbers);
                results.add(fourNumbers);
                leftIndex += 1;
            }
            else if (currentSum < target) {
                leftIndex += 1;
            } else {
                rightIndex -= 1;
            }
        }

        return new ArrayList<>(results);

    }



}

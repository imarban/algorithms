/*
Given the following structure in pseudo Code

http://stackoverflow.com/questions/184710/what-is-the-difference-between-a-deep-copy-and-a-shallow-copy

Node {
	integer value;
	List[Node]  adjacents;
}
*/


public class DeepCopy {

    public static Node deepcopy(Node node) {

        Node newNode = new Node(node.getValue(), new ArrayList<>());
        Map<Node, Node> copies = new IdentityHashMap<>();
        copies.put(node, newNode);
        for (Node n : node.getAdjacents()) {
            newNode.getAdjacents().add(deepcopy(n, copies));
        }
        
        return newNode;
    }

    private static Node deepcopy(Node node, Map<Node, Node> copies) {
        
        if (copies.get(node) == null) {
            Node nodeCopied = new Node(node.getValue(), new ArrayList<>());
            copies.put(node, nodeCopied);
            for (Node adjacent : node.getAdjacents()) {
                nodeCopied.getAdjacents().add(deepcopy(adjacent, copies));
            }
        }

        return copies.get(node);
    }
}
'''Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its
neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}

https://leetcode.com/problems/clone-graph/
'''


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
	def cloneGraph(self, node: 'Node') -> 'Node':
		if not node:
			return None
		copy = Node(node.val, [])

		q = [node]
		copy_dict = {node: Node(node.val)}

		while q:
			curr = q.pop(0)
			for nbr in curr.neighbors:
				if nbr not in copy_dict:
					copy_dict[nbr] = Node(nbr.val)
					q.append(nbr)
				copy_dict[curr].neighbors.append(copy_dict[nbr])

		return copy_dict[node]

# 1261. Find Elements in a Contaminated Binary Tree

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/](https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/)  
**Topics:** Hash Table, Tree, Depth-First Search, Breadth-First Search, Design, Binary Tree

---

## 📝 Problem Statement

Given a binary tree with the following rules:

	- `root.val == 0`

	For any `treeNode`:
	
		- If `treeNode.val` has a value `x` and `treeNode.left != null`, then `treeNode.left.val == 2 * x + 1`

		- If `treeNode.val` has a value `x` and `treeNode.right != null`, then `treeNode.right.val == 2 * x + 2`

	
	

Now the binary tree is contaminated, which means all `treeNode.val` have been changed to `-1`.

Implement the `FindElements` class:

	- `FindElements(TreeNode* root)` Initializes the object with a contaminated binary tree and recovers it.

	- `bool find(int target)` Returns `true` if the `target` value exists in the recovered binary tree.

 
Example 1:

```

**Input**
["FindElements","find","find"]
[[[-1,null,-1]],[1],[2]]
**Output**
[null,false,true]
**Explanation**
FindElements findElements = new FindElements([-1,null,-1]); 
findElements.find(1); // return False 
findElements.find(2); // return True 
```

Example 2:

```

**Input**
["FindElements","find","find","find"]
[[[-1,-1,-1,-1,-1]],[1],[3],[5]]
**Output**
[null,true,true,false]
**Explanation**
FindElements findElements = new FindElements([-1,-1,-1,-1,-1]);
findElements.find(1); // return True
findElements.find(3); // return True
findElements.find(5); // return False
```

Example 3:

```

**Input**
["FindElements","find","find","find","find"]
[[[-1,null,-1,-1,null,-1]],[2],[3],[4],[5]]
**Output**
[null,true,false,false,true]
**Explanation**
FindElements findElements = new FindElements([-1,null,-1,-1,null,-1]);
findElements.find(2); // return True
findElements.find(3); // return False
findElements.find(4); // return False
findElements.find(5); // return True

```

 
**Constraints:**

	- `TreeNode.val == -1`

	- The height of the binary tree is less than or equal to `20`

	- The total number of nodes is between `[1, 104]`

	- Total calls of `find()` is between `[1, 104]`

	- `0 6`

---

## 💻 Implementation (python3)

```py
class FindElements:

    def __init__(self, root: TreeNode | None):
        """
        Recovers the contaminated tree and indexes all existing values.
        Time Complexity: O(N) where N is the number of nodes in the tree.
        Space Complexity: O(N) to store values in a hash set.
        """
        self.seen: set[int] = set()
        
        if root is not None:
            root.val = 0
            self._recover(root)

    def _recover(self, node: TreeNode) -> None:
        """
        DFS traversal to restore node values and populate the lookup set.
        """
        self.seen.add(node.val)
        
        if node.left is not None:
            node.left.val = 2 * node.val + 1
            self._recover(node.left)
            
        if node.right is not None:
            node.right.val = 2 * node.val + 2
            self._recover(node.right)

    def find(self, target: int) -> bool:
        """
        Checks if the target value exists in the recovered binary tree.
        Time Complexity: O(1) average.
        Space Complexity: O(1).
        """
        return target in self.seen
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem presents a contaminated binary tree where all node values are set to `-1`. We are given deterministic rules for recovering the values:
1. `root.val = 0`
2. For any node with value `x`:
   - `node.left.val = 2 * x + 1`
   - `node.right.val = 2 * x + 2`

We need to answer membership queries: `find(target) -> bool`.

There are two primary paradigms to solve this:
1. **Hash Set Approach (Optimal for Query Time)**:
   - Traverse the tree once using DFS or BFS during initialization.
   - Recover each node's value in-place according to the formulas.
   - Insert every recovered value into a hash set (`self.seen`).
   - `find()` becomes a simple $O(1)$ hash set lookup.

2. **Bit Manipulation / Path Navigation Approach (Optimal for Auxiliary Space)**:
   - Notice the binary representation pattern if we shift values by 1:
     - `root.val + 1 = 1` (binary `1`)
     - `left.val + 1 = 2 * x + 2 = 2 * (x + 1)` (equivalent to appending bit `0`)
     - `right.val + 1 = 2 * x + 3 = 2 * (x + 1) + 1` (equivalent to appending bit `1`)
   - For any `target`, `target + 1` in binary represents the exact navigational path from the root (excluding the leading MSB `1`): `0` means step left, `1` means step right.
   - This allows $O(h)$ query time ($h \le 20$) with $O(1)$ auxiliary space without storing a set.

Given that $N \le 10^4$ and `find()` is called up to $10^4$ times, the Hash Set approach achieves $O(1)$ time per query with minimal space overhead ($\approx 10^4$ integers $\approx$ a few hundred kilobytes), making it the most practical production-ready choice.

---

### Step-by-Step Approach

1. **Initialization (`__init__`)**:
   - Initialize an empty hash set `self.seen`.
   - If `root` is not `None`, set `root.val = 0` and begin recursive DFS.
2. **DFS Tree Recovery (`_recover`)**:
   - Add the current `node.val` to `self.seen`.
   - If `node.left` exists, assign `node.left.val = 2 * node.val + 1` and recursively recover `node.left`.
   - If `node.right` exists, assign `node.right.val = 2 * node.val + 2` and recursively recover `node.right`.
3. **Lookup (`find`)**:
   - Check if `target` exists in `self.seen` using Python's $O(1)$ set membership test.

---

### Complexity Analysis

- **Time Complexity**:
  - `__init__`: $\mathcal{O}(N)$, where $N$ is the number of nodes in the binary tree. Each node is visited once during the DFS traversal.
  - `find`: $\mathcal{O}(1)$ average time complexity for hash set lookup.
- **Space Complexity**:
  - Overall Space: $\mathcal{O}(N)$ to store $N$ node values in `self.seen` plus $\mathcal{O}(h)$ call stack space during DFS, where $h \le 20$ is the height of the tree.
  - Auxiliary Space for `find()`: $\mathcal{O}(1)$.

---

### Common Pitfalls / Mistakes Candidates Make

1. **Re-searching the Tree on Every `find()` Call**:
   - Performing a BFS/DFS over the tree for every `find()` query results in $\mathcal{O}(N)$ per query, causing $\mathcal{O}(Q \times N) \approx 10^8$ operations, which risks a Time Limit Exceeded (TLE).
2. **Forgetting to Actually Recover the Tree**:
   - Although some automated test suites only test `find()`, the prompt explicitly requires recovering the contaminated tree. In a real Google/Meta interview, mutating the tree values as specified is expected.
3. **Recursion Stack Overflow**:
   - While tree height here is bounded by $20$, in general binary trees it can be $\mathcal{O}(N)$ if unbalanced. Always confirm maximum tree height with the interviewer.

---

### Real Interview Follow-Up Questions

#### 1. What if memory constraints are extremely tight (e.g., embedded environment with $O(1)$ extra memory)?
**Answer**:
Use the binary path navigation trick mentioned in the intuition:
- For `find(target)`: compute $V = target + 1$.
- Convert $V$ to its binary representation (e.g., using `bin(target + 1)[3:]` to strip `'0b1'`).
- Traverse down the tree starting from `root`: for each bit, step left if `'0'`, or right if `'1'`. If the child is `None` at any step, return `False`. If the path completes, return `True`.
- This eliminates the $\mathcal{O}(N)$ hash set entirely, achieving $\mathcal{O}(1)$ auxiliary space and $\mathcal{O}(h)$ time per query (at most 20 pointer hops).

#### 2. How would you handle a concurrent environment where multiple threads call `find()` simultaneously?
**Answer**:
- If the tree is recovered and immutable after `__init__`, reading from `self.seen` is thread-safe for concurrent readers in Python (and in C++/Java using immutable/read-only structures).
- If trees can be dynamically updated (nodes added/removed after initialization), use a read-write lock (`threading.RWLock`) or concurrent hash map (`ConcurrentHashMap` in Java) to allow concurrent reads while synchronizing writes.

#### 3. What if `target` can exceed standard 64-bit integer limits?
**Answer**:
- In Python, integers have arbitrary precision by default, so arithmetic overflow is avoided.
- In languages like C++ or Java, `target + 1` could overflow a 64-bit unsigned integer if the tree height exceeds 63. BigInt or bitset representations would be necessary.

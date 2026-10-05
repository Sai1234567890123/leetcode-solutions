# 1028. Recover a Tree From Preorder Traversal

**Difficulty:** Hard  
**LeetCode Link:** [https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/](https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/)  
**Topics:** String, Tree, Depth-First Search, Binary Tree

---

## 📝 Problem Statement

We run a preorder depth-first search (DFS) on the `root` of a binary tree.

At each node in this traversal, we output `D` dashes (where `D` is the depth of this node), then we output the value of this node.  If the depth of a node is `D`, the depth of its immediate child is `D + 1`.  The depth of the `root` node is `0`.

If a node has only one child, that child is guaranteed to be **the left child**.

Given the output `traversal` of this traversal, recover the tree and return *its* `root`.

 
Example 1:

```

**Input:** traversal = "1-2--3--4-5--6--7"
**Output:** [1,2,5,3,4,6,7]

```

Example 2:

```

**Input:** traversal = "1-2--3---4-5--6---7"
**Output:** [1,2,5,3,null,6,null,4,null,7]

```

Example 3:

```

**Input:** traversal = "1-401--349---90--88"
**Output:** [1,401,null,349,88,90]

```

 
**Constraints:**

	- The number of nodes in the original tree is in the range `[1, 1000]`.

	- `1 9`

---

## 💻 Implementation (python3)

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverFromPreorder(self, traversal: str) -> TreeNode | None:
        stack: list[TreeNode] = []
        i = 0
        n = len(traversal)
        
        while i < n:
            # Step 1: Count the number of dashes to determine depth
            depth = 0
            while i < n and traversal[i] == '-':
                depth += 1
                i += 1
            
            # Step 2: Parse the node's integer value
            val = 0
            while i < n and traversal[i].isdigit():
                val = val * 10 + int(traversal[i])
                i += 1
            
            node = TreeNode(val)
            
            # Step 3: Maintain the stack such that stack size matches current depth
            # The node at stack[depth - 1] must be the parent of the current node
            while len(stack) > depth:
                stack.pop()
            
            # Step 4: Attach the node to its parent
            if stack:
                if stack[-1].left is None:
                    stack[-1].left = node
                else:
                    stack[-1].right = node
            
            # Step 5: Push current node onto stack
            stack.append(node)
        
        # The root node is always at the bottom of the stack
        return stack[0] if stack else None
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem gives a serialized binary tree where each node's preorder DFS visit is preceded by $D$ dashes, representing its depth in the tree. Because the traversal is strictly preorder (Parent $\to$ Left $\to$ Right):
1. A node at depth $D$ is always a child of the most recently visited node at depth $D - 1$.
2. If the parent doesn't have a left child yet, this node must be its left child. Otherwise, it must be the right child (guaranteed by problem constraints).

This property naturally maps to an explicit **Stack**:
- The stack maintains the active path of ancestors from the root down to the current node.
- The size of the stack at any point represents the depth of the next child to be inserted.
- If the current node's depth is less than the current stack size, we have finished exploring subtrees and must pop elements until `len(stack) == depth`. The element at `stack[-1]` is then guaranteed to be the direct parent.

### Step-by-Step Approach

1. **Parse `depth` and `val` sequentially**:
   - Count consecutive `'-'` characters to get `depth`.
   - Parse consecutive digits to form the integer `val`.
2. **Backtrack via Stack**:
   - While `len(stack) > depth`, pop nodes from the stack.
3. **Attach to Parent**:
   - If the stack is non-empty, inspect `stack[-1]`. If `stack[-1].left` is `None`, set `stack[-1].left = node`. Otherwise, set `stack[-1].right = node`.
4. **Push Current Node**:
   - Append the newly created `TreeNode(val)` to the stack.
5. **Return Root**:
   - The root of the tree is the very first node pushed, which remains at `stack[0]`.

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$, where $N$ is the length of the string `traversal`. Each character in the string is visited a constant number of times during parsing. Each node is pushed and popped from the stack at most once.
- **Space Complexity:** $\mathcal{O}(H)$, where $H$ is the maximum depth (height) of the binary tree. In the worst case (a completely skewed tree), $H \le V$ (where $V$ is the number of nodes), leading to $\mathcal{O}(V)$ auxiliary space for the stack.

### Common Pitfalls / Mistakes

1. **Multi-digit numbers**: Assuming single-digit values. Values can be up to $10^9$, requiring reading characters until the next dash or end of string.
2. **String splitting errors**: Attempting `traversal.split('-')` or naive regex can be tricky and inefficient because dashes are delimiters of variable lengths and cannot simply be treated as single-character separators.
3. **Left vs. Right Assignment**: Not honoring the specification that if a node has only one child, it must be the left child. Checking `stack[-1].left is None` properly ensures this.

### Real Interview Follow-Up Questions

1. **What if the string is streamed over a network rather than given upfront?**
   - *Answer:* The algorithm is already streaming-friendly. We can parse tokens `(depth, val)` on the fly from an iterator or stream buffer without loading the entire string into memory. Memory overhead remains $\mathcal{O}(H)$ instead of $\mathcal{O}(N)$.

2. **Can this be solved recursively without an explicit stack?**
   - *Answer:* Yes. We can maintain a global/mutable index pointer. A recursive function `helper(expected_depth)` peaks at the next depth. If the next depth matches `expected_depth`, it consumes the token, creates the node, and recursively calls `helper(expected_depth + 1)` for both left and right children.

3. **What if the values could be negative?**
   - *Answer:* If values can be negative, a dash `'-'` could represent both depth indentation and a negative sign. However, since node values are preceded by at least one dash (unless it's the root), ambiguity could arise if negative signs aren't disambiguated. We would need a lookahead: once the sequence of depth dashes ends and digits begin, an extra dash immediately preceding digits signifies negation, or the format would need explicit separators (e.g., parentheses or commas).

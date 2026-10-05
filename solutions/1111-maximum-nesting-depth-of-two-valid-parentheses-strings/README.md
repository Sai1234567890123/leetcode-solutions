# 1111. Maximum Nesting Depth of Two Valid Parentheses Strings

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/](https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/)  
**Topics:** String, Stack, Bracket Sequences

---

## 📝 Problem Statement

A string is a *valid parentheses string* (denoted VPS) if and only if it consists of `"("` and `")"` characters only, and:

	- It is the empty string, or

	- It can be written as `AB` (`A` concatenated with `B`), where `A` and `B` are VPS's, or

	- It can be written as `(A)`, where `A` is a VPS.

We can similarly define the *nesting depth* `depth(S)` of any VPS `S` as follows:

	- `depth("") = 0`

	- `depth(A + B) = max(depth(A), depth(B))`, where `A` and `B` are VPS's

	- `depth("(" + A + ")") = 1 + depth(A)`, where `A` is a VPS.

For example, `""`, `"()()"`, and `"()(()())"` are VPS's (with nesting depths 0, 1, and 2), and `")("` and `"(()"` are not VPS's.

Given a VPS seq, split it into two disjoint subsequences `A` and `B`, such that `A` and `B` are VPS's (and `A.length + B.length = seq.length`). The subsequences may not necessarily be contiguous.

For example, for the sequence `123456789`, one possible split is:

	
	A = {1, 3, 5, 7, 9},
	
	
	B = {2, 4, 6, 8}.
	

This corresponds to the output `[0, 1, 0, 1, 0, 1, 0, 1, 0]`  where 0 indicates membership in A and 1 indicates membership in B.

Now choose **any** such `A` and `B` such that `max(depth(A), depth(B))` is the minimum possible value.

Return an `answer` array (of length `seq.length`) that encodes such a choice of `A` and `B`:  `answer[i] = 0` if `seq[i]` is part of `A`, else `answer[i] = 1`.  Note that even though multiple answers may exist, you may return any of them.

 
Example 1:

```

**Input:** seq = "(()())"
**Output:** [0,1,1,1,1,0]

```

Example 2:

```

**Input:** seq = "()(())()"
**Output:** [0,0,0,1,1,0,1,1]

```

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        ans = []
        depth = 0
        
        for ch in seq:
            if ch == '(':
                # Assign '(' based on the current nesting level before incrementing
                ans.append(depth % 2)
                depth += 1
            else:
                # Decrement depth first so ')' matches the depth of its corresponding '('
                depth -= 1
                ans.append(depth % 2)
                
        return ans
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks us to split a Valid Parentheses String (VPS) `seq` into two disjoint subsequences, $A$ and $B$, such that both $A$ and $B$ are valid parentheses strings and $\max(\text{depth}(A), \text{depth}(B))$ is minimized.

If the original string has maximum nesting depth $D$, the theoretical lower bound for the maximum depth of the two split subsequences is $\lceil D / 2 \rceil$. 

To achieve this lower bound:
- Parentheses at odd nesting levels can be assigned to subsequence $A$.
- Parentheses at even nesting levels can be assigned to subsequence $B$.

By alternating the assignment based on the depth parity:
1. Every matching pair of `(` and `)` resides at the exact same depth level and is therefore routed to the same subsequence, preserving the validity of both VPS subsequences.
2. The nested layers alternate between $A$ and $B$, effectively halving the maximum nesting depth for both strings.

### Step-by-Step Approach

1. Initialize `depth = 0` to track the current nesting depth.
2. Iterate through each character `ch` in `seq`:
   - If `ch == '('`:
     - Its depth level is the current value of `depth`.
     - Assign it to group `depth % 2`.
     - Increment `depth` by 1.
   - If `ch == ')'`:
     - Decrement `depth` by 1 first so that it matches the depth of its opening counterpart.
     - Assign it to group `depth % 2`.
3. Return the populated result array.

### Complexity Analysis

- **Time Complexity:** $O(n)$ where $n$ is the length of `seq`. We perform a single linear scan through the string, performing $O(1)$ work per character.
- **Space Complexity:** $O(1)$ auxiliary space. The output array takes $O(n)$ space, which is required to return the answer.

### Common Pitfalls / Mistakes Candidates Make

1. **Splitting contiguously vs. subsequences:** A common misunderstanding is assuming $A$ and $B$ must be contiguous substrings (e.g., prefix and suffix). The problem explicitly defines them as *subsequences*, allowing arbitrary interleaved indices.
2. **Assigning opening and closing brackets to different groups:** If the depth update order isn't synchronized between `(` and `)`, a pair `()` might have its opening bracket at depth $0$ and closing bracket assigned based on depth $1$, sending them to different subsequences and invalidating the VPS property.
3. **Overcomplicating with Stack or Two-Pass Algorithms:** Candidates often try to compute the global max depth first using a stack, find pairs, and then perform a second pass. A single pass using simple parity tracking is strictly optimal and sufficient.

### Real Interview Follow-Up Questions & Answers

#### 1. Can we split into $K$ disjoint VPS strings instead of 2?
**Answer:** Yes. The exact same parity concept generalizes to modular arithmetic modulo $K$. We route brackets at nesting level `depth` to group `depth % K`. This achieves an optimal maximum depth of $\lceil D / K \rceil$.

#### 2. What if the input is a continuous data stream of brackets?
**Answer:** The algorithm naturally supports streaming. Since each character's output depends purely on the scalar state variable `depth` and the incoming character itself, we can process brackets one-by-one in $O(1)$ time and $O(1)$ memory without needing to buffer the entire stream.

#### 3. Can this be solved in-place if the input is mutable?
**Answer:** If the input is passed as a mutable character array (or integer array), we can overwrite each character in-place with `'0'` / `'1'` or `0` / `1` respectively, requiring $0$ extra allocation.

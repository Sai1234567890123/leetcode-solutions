# 2181. Merge Nodes in Between Zeros

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/merge-nodes-in-between-zeros/](https://leetcode.com/problems/merge-nodes-in-between-zeros/)  
**Topics:** Linked List, Simulation

---

## 📝 Problem Statement

You are given the `head` of a linked list, which contains a series of integers **separated** by `0`'s. The **beginning** and **end** of the linked list will have `Node.val == 0`.

For **every **two consecutive `0`'s, **merge** all the nodes lying in between them into a single node whose value is the **sum** of all the merged nodes. The modified list should not contain any `0`'s.

Return *the* `head` *of the modified linked list*.

 
Example 1:

```

**Input:** head = [0,3,1,0,4,5,2,0]
**Output:** [4,11]
**Explanation:** 
The above figure represents the given linked list. The modified list contains
- The sum of the nodes marked in green: 3 + 1 = 4.
- The sum of the nodes marked in red: 4 + 5 + 2 = 11.

```

Example 2:

```

**Input:** head = [0,1,0,3,0,2,2,0]
**Output:** [1,3,4]
**Explanation:** 
The above figure represents the given linked list. The modified list contains
- The sum of the nodes marked in green: 1 = 1.
- The sum of the nodes marked in red: 3 = 3.
- The sum of the nodes marked in yellow: 2 + 2 = 4.

```

 
**Constraints:**

	- The number of nodes in the list is in the range `[3, 2 * 105]`.

	- `0

---

## 💻 Implementation (python3)

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeNodes(self, head: ListNode | None) -> ListNode | None:
        """
        Merges nodes between 0s in-place with O(1) auxiliary space.
        Modifies the values of existing nodes and rewires 'next' pointers.
        """
        # modify_ptr will point to the node where the current block's sum is stored.
        # Since the list starts with 0, head.next is the first non-zero node.
        modify_ptr = head.next
        curr = head.next
        
        running_sum = 0
        
        while curr:
            if curr.val != 0:
                running_sum += curr.val
                curr = curr.next
            else:
                # Reached the delimiter 0
                modify_ptr.val = running_sum
                running_sum = 0
                
                # If there are subsequent blocks (curr.next is not None),
                # link modify_ptr to the start of the next block.
                # Otherwise, terminate the list.
                if curr.next is not None:
                    modify_ptr.next = curr.next
                    modify_ptr = modify_ptr.next
                    curr = curr.next
                else:
                    modify_ptr.next = None
                    break
                    
        return head.next
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem requires condensing segments of non-zero nodes delimited by `0`s into single nodes containing their sums. 
A naive approach would be allocating new `ListNode` instances for each sum and appending them to a new list, which requires $O(K)$ auxiliary space (where $K$ is the number of zero-delimited segments).

However, in production and interview environments (especially at Google and Meta), mutating the linked list **in-place** to achieve $O(1)$ auxiliary memory is the gold standard. 

We can maintain two pointers:
1. `modify_ptr`: Points to the node whose value will be overwritten with the merged sum.
2. `curr`: Traverses through the nodes to accumulate the segment sum.

By reusing existing nodes (specifically, the first non-zero node of each segment) and reconnecting their `.next` pointers, we avoid any dynamic memory allocation or garbage collection overhead.

---

### Step-by-Step Approach

1. **Initialization**:
   - `head` is guaranteed to be `0`, so the first segment starts at `head.next`.
   - Set `modify_ptr = head.next` and `curr = head.next`.
   - Maintain `running_sum = 0`.

2. **Traverse and Accumulate**:
   - While `curr` is not `None`:
     - If `curr.val != 0`, add `curr.val` to `running_sum` and move `curr = curr.next`.
     - If `curr.val == 0`, we have reached the end of the current segment:
       - Update `modify_ptr.val = running_sum`.
       - Reset `running_sum = 0`.
       - Check if this is the final `0` (`curr.next is None`):
         - If yes, set `modify_ptr.next = None` and break.
         - If no, connect `modify_ptr.next` to `curr.next` (the start of the next segment), advance `modify_ptr` to `curr.next`, and advance `curr` to `curr.next`.

3. **Return**:
   - Return `head.next` since `head.next` contains the sum of the first segment.

---

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$, where $N$ is the number of nodes in the linked list. The `curr` pointer visits every node in the linked list exactly once.
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary space. The algorithm reuses existing list nodes and mutates values/pointers in place without allocating any new objects.

---

### Common Pitfalls / Mistakes Candidates Make

1. **Memory Allocation**: Creating new `ListNode` instances for every sum instead of reusing existing nodes. While accepted, it fails follow-up questions regarding strict memory efficiency and garbage collector load.
2. **Trailing Pointer Dangling**: Forgetting to set `modify_ptr.next = None` at the end of the list. This leaves the old tail attached, causing cycles or extraneous nodes.
3. **Handling the Dummy Head / Tail**: Attempting to include the leading `0` node in the final list or misinterpreting the final `0` as the start of an empty segment.

---

### Real Interview Follow-Up Questions & Answers

#### 1. What if memory cannot be modified in-place (read-only input)?
* **Answer**: If the input nodes are immutable (e.g., shared across threads or stored in shared memory), in-place mutation is prohibited. In that case, use a dummy head node and dynamically allocate a new `ListNode(running_sum)` whenever a `0` is encountered, achieving $\mathcal{O}(K)$ auxiliary space (where $K$ is the number of segments).

#### 2. How would you handle a streaming / continuous linked list with unknown termination?
* **Answer**: Use a generator/iterator pattern. As the stream flows, maintain `running_sum`. Yield the sum whenever a delimiter `0` is received and reset the accumulator:
  ```python
  def stream_merged(stream):
      running_sum = 0
      for val in stream:
          if val == 0 and running_sum > 0:
              yield running_sum
              running_sum = 0
          else:
              running_sum += val
  ```

#### 3. How would you handle potential integer overflow for extremely large segments?
* **Answer**: In Python, integers have arbitrary precision, so overflow is handled automatically. In languages like C++ or Java, `running_sum` should be typed as a 64-bit integer (`long long` or `long`), and if constraints permit sums exceeding $2^{63}-1$, a `BigInteger` representation or custom overflow-checked arithmetic would be required.

# 0237. Delete Node in a Linked List

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/delete-node-in-a-linked-list/](https://leetcode.com/problems/delete-node-in-a-linked-list/)  
**Topics:** Linked List

---

## 📝 Problem Statement

There is a singly-linked list `head` and we want to delete a node `node` in it.

You are given the node to be deleted `node`. You will **not be given access** to the first node of `head`.

All the values of the linked list are **unique**, and it is guaranteed that the given node `node` is not the last node in the linked list.

Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:

	- The value of the given node should not exist in the linked list.

	- The number of nodes in the linked list should decrease by one.

	- All the values before `node` should be in the same order.

	- All the values after `node` should be in the same order.

**Custom testing:**

	- For the input, you should provide the entire linked list `head` and the node to be given `node`. `node` should not be the last node of the list and should be an actual node in the list.

	- We will build the linked list and pass the node to your function.

	- The output will be the entire list after calling your function.

 
Example 1:

```

**Input:** head = [4,5,1,9], node = 5
**Output:** [4,1,9]
**Explanation: **You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.

```

Example 2:

```

**Input:** head = [4,5,1,9], node = 1
**Output:** [4,5,9]
**Explanation: **You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.

```

 
**Constraints:**

	- The number of the nodes in the given list is in the range `[2, 1000]`.

	- `-1000

---

## 💻 Implementation (python3)

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node: ListNode) -> None:
        """
        Deletes the given node from a singly-linked list in-place.
        Modifies node directly; does not return anything.
        """
        # Since we cannot modify the previous node's `next` pointer,
        # we copy the value of the next node into the current node.
        node.val = node.next.val
        
        # Bypass the next node, effectively deleting it from the list.
        node.next = node.next.next
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

In a standard singly linked list deletion, to delete node `C` from `A -> B -> C -> D`, we need a pointer to node `B` so we can update `B.next = C.next`. However, here we are only given a reference to `C` (the node to delete) and **no reference to the `head`** of the list. In a singly linked list, it is impossible to traverse backwards to reach node `B`.

Since the problem statement clarifies that:
1. Deleting does not require freeing the exact memory location of `node`.
2. `node` is guaranteed not to be the tail (`node.next` is never `None`).

We can reframe the problem: instead of physically removing `node`, we can overwrite `node`'s value with the next node's value (`node.next.val`) and then skip `node.next` by pointing `node.next` to `node.next.next`. From an external observer's standpoint, `node`'s original value has vanished, the list length is reduced by 1, and the order of all other elements is preserved.

---

### Step-by-Step Approach

1. **Copy Value:** Set `node.val = node.next.val`.
2. **Rewire Pointer:** Set `node.next = node.next.next`.
3. The garbage collector (in Python) will reclaim the skipped node since it no longer has incoming references (assuming no external references exist).

---

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(1)$. The operation involves exactly one value assignment and one pointer reassignment, executing in strictly constant time.
- **Space Complexity:** $\mathcal{O}(1)$. No additional memory or data structures are allocated.

---

### Common Pitfalls / Mistakes Candidates Make

1. **Attempting to iterate backwards:** Candidates often freeze or try to find a way to access previous nodes, forgetting that singly linked lists are strictly unidirectional.
2. **Forgetting the tail constraint:** Candidates might write this solution without recognizing why the problem guarantees `node` is not the tail. If `node` were the tail (`node.next is None`), this approach would throw a `NullPointerException` / `AttributeError`. A tail node cannot be deleted in $\mathcal{O}(1)$ without a doubly-linked structure or a pointer to the previous node.
3. **Misinterpreting "deletion":** Spending time trying to deallocate or free memory in low-level languages (like C/C++) while leaving dangling pointers elsewhere.

---

### Real Interview Follow-Up Questions & Answers

#### 1. What if `node` IS the tail node? Can we still delete it without the `head`?
**Answer:** In a standard singly linked list, **no**, it is mathematically impossible. If we set `node = None`, we only modify the local variable `node`, not the `next` pointer of the predecessor pointing to it. To delete the tail, we must either:
- Have a pointer to `head` to traverse to the node preceding the tail ($\mathcal{O}(n)$).
- Use a doubly linked list ($\mathcal{O}(1)$).
- Use a dummy/sentinel node with circular wrapping (problem-dependent).

#### 2. What are the side effects of this approach in a real-world system?
**Answer:**
- **External References:** If another part of the system or thread holds a reference to `node.next`, that object has now been bypassed and decoupled from the list, but its old data now lives inside `node`. Anyone holding a reference to `node` will observe an unexpected mutation of its value.
- **Object Identity:** In languages like Java or Python, object identity (`id(node)`) changes context. Code relying on reference equality (`nodeA == nodeB`) may break because the node containing the value was swapped.

#### 3. How would you handle this in a concurrent environment?
**Answer:**
Modifying both `node.val` and `node.next` is not an atomic operation. A concurrent reader could read the new `val` while `node.next` still points to the old next node (duplicate data temporarily visible). To make it thread-safe:
- Acquire a fine-grained mutex/lock on `node` and `node.next`.
- Or use atomic compare-and-swap (CAS) operations if supported, although multi-field updates typically require transactional memory or locking.

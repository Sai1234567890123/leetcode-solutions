# 0950. Reveal Cards In Increasing Order

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/reveal-cards-in-increasing-order/](https://leetcode.com/problems/reveal-cards-in-increasing-order/)  
**Topics:** Array, Queue, Sorting, Simulation

---

## 📝 Problem Statement

You are given an integer array `deck`. There is a deck of cards where every card has a unique integer. The integer on the `ith` card is `deck[i]`.

You can order the deck in any order you want. Initially, all the cards start face down (unrevealed) in one deck.

You will do the following steps repeatedly until all cards are revealed:

	- Take the top card of the deck, reveal it, and take it out of the deck.

	- If there are still cards in the deck then put the next top card of the deck at the bottom of the deck.

	- If there are still unrevealed cards, go back to step 1. Otherwise, stop.

Return *an ordering of the deck that would reveal the cards in increasing order*.

**Note** that the first entry in the answer is considered to be the top of the deck.

 
Example 1:

```

**Input:** deck = [17,13,11,2,3,5,7]
**Output:** [2,13,3,11,5,17,7]
**Explanation:** 
We get the deck in the order [17,13,11,2,3,5,7] (this order does not matter), and reorder it.
After reordering, the deck starts as [2,13,3,11,5,17,7], where 2 is the top of the deck.
We reveal 2, and move 13 to the bottom.  The deck is now [3,11,5,17,7,13].
We reveal 3, and move 11 to the bottom.  The deck is now [5,17,7,13,11].
We reveal 5, and move 17 to the bottom.  The deck is now [7,13,11,17].
We reveal 7, and move 13 to the bottom.  The deck is now [11,17,13].
We reveal 11, and move 17 to the bottom.  The deck is now [13,17].
We reveal 13, and move 17 to the bottom.  The deck is now [17].
We reveal 17.
Since all the cards revealed are in increasing order, the answer is correct.

```

Example 2:

```

**Input:** deck = [1,1000]
**Output:** [1,1000]

```

 
**Constraints:**

	- `1 6`

	- All the values of `deck` are **unique**.

---

## 💻 Implementation (python3)

```py
from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        n = len(deck)
        # Sort the deck so we can place cards in increasing order
        sorted_deck = sorted(deck)

        # Use a queue to simulate the card-revealing process on indices
        index_queue = deque(range(n))
        result = [0] * n

        for card in sorted_deck:
            # The next revealed slot gets the smallest available card
            reveal_idx = index_queue.popleft()
            result[reveal_idx] = card

            # Move the next top index to the bottom of the deck if cards remain
            if index_queue:
                index_queue.append(index_queue.popleft())

        return result
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem defines a deterministic simulation where:
1. The top card is revealed and removed.
2. The next top card is moved to the bottom.
3. The process repeats until no cards remain.

We want the cards to be revealed in strictly ascending order. Rather than trying to reverse-engineer the values mathematically in-place, we can simulate the process on the **indices** of the deck:
- Suppose the deck has length $N$. Initially, the indices in order from top to bottom are $[0, 1, 2, \dots, N - 1]$.
- Simulating the exact rules on these indices reveals which index in the original array gets revealed at step $0$, which at step $1$, and so on.
- Since we want the cards to be revealed in sorted order, we sort the input deck: `sorted_deck = sorted(deck)`.
- At each step $i$, we map the card `sorted_deck[i]` directly to the simulated index that is revealed at that step.

An alternative viewpoint is to work backwards from an empty deck:
- Sort the cards in descending order.
- For each card, rotate the bottom card to the top, then put the current card on top.
Both approaches achieve identical $O(N \log N)$ complexity, but simulating index order forward is often more intuitive to explain and less error-prone to implement.

---

### Step-by-Step Approach

1. **Sort the Deck**: Sort `deck` in ascending order.
2. **Initialize Queue**: Populate a double-ended queue (`deque`) with indices from `0` to `N - 1`.
3. **Simulate & Assign**:
   - For each `card` in `sorted_deck`:
     - Pop the front index from the queue (`reveal_idx = queue.popleft()`).
     - Assign `result[reveal_idx] = card`.
     - If the queue is not empty, pop the next front index and push it to the back (`queue.append(queue.popleft())`).
4. **Return Result**: The `result` array now contains the deck in the required starting arrangement.

---

### Complexity Analysis

- **Time Complexity:** $O(N \log N)$
  - Sorting the array takes $O(N \log N)$ time.
  - The queue simulation performs $2N - 1$ operations (each `popleft` and `append` on `collections.deque` is $O(1)$ amortized/worst-case).
  - Overall Time: $O(N \log N)$, which is optimal due to the comparison-based sorting lower bound.

- **Space Complexity:** $O(N)$
  - The `result` array requires $O(N)$ space.
  - The `index_queue` stores at most $N$ integers, requiring $O(N)$ auxiliary space.
  - Overall Auxiliary Space: $O(N)$.

---

### Common Pitfalls / Mistakes

1. **Using a standard list as a queue**:
   - Doing `list.pop(0)` in Python takes $O(N)$ time per operation, causing the simulation to degrade to $O(N^2)$. Always use `collections.deque` for $O(1)$ operations from both ends.
2. **Missing the "queue not empty" check**:
   - Forgetting to check `if index_queue:` before moving the next index to the bottom leads to an `IndexError` on the very last card.
3. **Confusing indices with card values**:
   - Trying to simulate with the actual card values directly without sorting or reverse simulation leads to complex off-by-one errors. Decoupling the simulation using indices makes the code clean and bug-free.

---

### Real Interview Follow-Up Questions

#### 1. What if $N$ is massive (e.g., $10^7$) and integers are bounded in range $[1, K]$ where $K \ll N$?
- **Answer:** If numbers are within a small range, we can replace the comparison sort with **Counting Sort** or **Radix Sort**, reducing the sorting phase to $O(N)$. The simulation phase remains $O(N)$, bringing the overall time complexity to $O(N)$ and space to $O(N)$.

#### 2. Can we solve this problem in $O(1)$ auxiliary space (in-place)?
- **Answer:**
  - Standard in-place sorting takes $O(\log N)$ space.
  - For the index permutation, finding the cycle decomposition or using index-encoding tricks (e.g., storing `new_val * M + old_val`) can allow placing values without an external queue or result array, but the cyclic index movement of Josephus-style elimination makes an $O(1)$ auxiliary space forward simulation complex.
  - Alternatively, doing the reverse simulation directly in-place with a circular buffer can achieve $O(1)$ auxiliary space if memory outside the returned container is constrained.

#### 3. How does this problem relate to the Josephus Problem?
- **Answer:** This is a variant of the Josephus problem with step size $k = 2$. In standard Josephus, every $k$-th element is eliminated. Here, every alternating card is eliminated (revealed), while skipped cards are rotated to the end. The exact position of any card can be derived mathematically using binary representations (e.g., bitwise rotations), which allows computing the index for any specific rank $i$ in $O(1)$ time without full queue simulation.

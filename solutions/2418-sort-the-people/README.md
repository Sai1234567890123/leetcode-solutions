# 2418. Sort the People

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/sort-the-people/](https://leetcode.com/problems/sort-the-people/)  
**Topics:** Array, Hash Table, String, Sorting

---

## 📝 Problem Statement

You are given an array of strings `names`, and an array `heights` that consists of **distinct** positive integers. Both arrays are of length `n`.

For each index `i`, `names[i]` and `heights[i]` denote the name and height of the `ith` person.

Return `names`* sorted in **descending** order by the people's heights*.

 
Example 1:

```

**Input:** names = ["Mary","John","Emma"], heights = [180,165,170]
**Output:** ["Mary","Emma","John"]
**Explanation:** Mary is the tallest, followed by Emma and John.

```

Example 2:

```

**Input:** names = ["Alice","Bob","Bob"], heights = [155,185,150]
**Output:** ["Bob","Alice","Bob"]
**Explanation:** The first Bob is the tallest, followed by Alice and the second Bob.

```

 
**Constraints:**

	- `n == names.length == heights.length`

	- `1 3`

	- `1 5`

	- `names[i]` consists of lower and upper case English letters.

	- All the values of `heights` are distinct.

---

## 💻 Implementation (python3)

```py
class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        """
        Sorts the array of names based on the corresponding heights in descending order.
        
        Args:
            names: list[str] - Names of the people.
            heights: list[int] - Distinct heights corresponding to each person.
            
        Returns:
            list[str] - Names sorted in descending order of heights.
        """
        # Pair each height with its corresponding name, sort in reverse (descending) order by height,
        # and extract only the names.
        return [name for _, name in sorted(zip(heights, names), reverse=True)]
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks us to reorder an array of names based on a secondary key: the `heights` array, sorted in descending order. 

In Python, the most idiomatic and efficient approach is to combine the two lists using `zip(heights, names)`. By placing `heights` as the first element of each tuple, Python's default lexicographical tuple comparison will naturally sort primarily by height. Setting `reverse=True` ensures we sort from tallest to shortest. Once sorted, a list comprehension extracts the names.

Alternative approaches include:
1. **Hash Map / Dictionary**: Since all heights are distinct, we could map `height -> name`, sort the keys in descending order, and retrieve the names. This uses $O(n \log n)$ time and $O(n)$ space.
2. **Index Array**: Sorting indices `0` to `n-1` based on `heights[i]` descending and mapping back to `names[i]`. This avoids creating tuples.
3. **Counting Sort / Bucket Sort**: Since heights are bounded (up to $10^5$), we could technically sort in $O(n + \max(heights))$ time, but for $n \le 10^3$, comparison-based sorting ($O(n \log n)$) via Timsort is significantly faster in practice and avoids allocating large sparse arrays.

### Step-by-Step Approach

1. Combine `heights` and `names` into pairs: `(heights[i], names[i])`.
2. Sort the pairs in descending order using `sorted(..., reverse=True)`. Python's Timsort operates in $O(n \log n)$ time.
3. Use a list comprehension to extract the second element (the `name`) from each sorted pair.
4. Return the resulting list.

### Complexity Analysis

- **Time Complexity:** $O(n \log n)$
  - Zipping two lists of length $n$ takes $O(n)$ time.
  - Sorting $n$ elements using Timsort takes $O(n \log n)$ comparisons and moves.
  - Extracting the sorted names takes $O(n)$ time.
  - Total Time: $O(n \log n)$, which is well within constraints for $n \le 10^3$.

- **Space Complexity:** $O(n)$
  - `zip(heights, names)` produces $n$ pairs during the sort.
  - Python's `sorted()` allocates $O(n)$ temporary space.
  - The output array requires $O(n)$ space to store the rearranged names.
  - Total Space: $O(n)$.

### Common Pitfalls / Mistakes Candidates Make

1. **Hash Map on Non-Distinct Keys:** Candidates frequently reach for a hash map (`{height: name}`) without checking if heights are guaranteed to be distinct. If duplicates were allowed, a standard dictionary would overwrite duplicate keys. While heights are distinct in this specific problem, using `zip` or index sorting is safer and generalizes better.
2. **Sorting `names` instead of `heights`:** Forgetting to place `height` as the primary sort key in tuple comparison (e.g., `zip(names, heights)` would sort alphabetically by name first).
3. **Over-engineering with Counting Sort:** Because $\max(heights) \le 10^5$, some candidates allocate an array of size $10^5 + 1$. While theoretically $O(n + M)$, it uses substantially more memory and runs slower for small $n$ ($n \le 10^3$) due to cache misses.

### Real Interview Follow-Up Questions

#### 1. What if heights are NOT distinct?
- **Answer:** If two people have the same height, the problem statement must specify a tie-breaking rule (e.g., keep original relative order, or sort names alphabetically).
  - If we want to preserve original relative order (stability): Python's Timsort is stable. We can sort indices `range(n)` using a custom key `key=lambda i: heights[i]` in reverse. Python preserves the original order for equal keys.
  - If tie-breaking by name: We can sort tuples `(-height, name)`.

#### 2. What if $n$ is very large (e.g., billions of people) and doesn't fit into memory?
- **Answer:** Use External Merge Sort:
  1. Stream data into memory in chunks that fit RAM.
  2. Sort each chunk in memory and write to temporary files on disk.
  3. Perform a $K$-way merge using a min/max-heap across the sorted temporary runs to produce the final sorted stream.

#### 3. What if we only need the top $K$ tallest people instead of sorting everyone?
- **Answer:** We can reduce the time complexity from $O(n \log n)$ to $O(n \log K)$ or $O(n)$:
  - Use a min-heap of size $K$ to maintain the $K$ largest elements in $O(n \log K)$ time.
  - Alternatively, use the Quickselect algorithm (`introselect`) to partition the top $K$ elements in $O(n)$ average time, then sort only those $K$ elements in $O(K \log K)$ time.

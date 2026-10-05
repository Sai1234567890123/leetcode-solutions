# 1773. Count Items Matching a Rule

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/count-items-matching-a-rule/](https://leetcode.com/problems/count-items-matching-a-rule/)  
**Topics:** Array, String

---

## 📝 Problem Statement

You are given an array `items`, where each `items[i] = [typei, colori, namei]` describes the type, color, and name of the `ith` item. You are also given a rule represented by two strings, `ruleKey` and `ruleValue`.

The `ith` item is said to match the rule if **one** of the following is true:

	- `ruleKey == "type"` and `ruleValue == typei`.

	- `ruleKey == "color"` and `ruleValue == colori`.

	- `ruleKey == "name"` and `ruleValue == namei`.

Return *the number of items that match the given rule*.

 
Example 1:

```

**Input:** items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"
**Output:** 1
**Explanation:** There is only one item matching the given rule, which is ["computer","silver","lenovo"].

```

Example 2:

```

**Input:** items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone"
**Output:** 2
**Explanation:** There are only two items matching the given rule, which are ["phone","blue","pixel"] and ["phone","gold","iphone"]. Note that the item ["computer","silver","phone"] does not match.
```

 
**Constraints:**

	- `1 4`

	- `1 i.length, colori.length, namei.length, ruleValue.length

---

## 💻 Implementation (python3)

```py
class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        # Map ruleKey to the corresponding index in each item tuple:
        # items[i] = [type_i, color_i, name_i]
        key_to_index = {
            "type": 0,
            "color": 1,
            "name": 2
        }
        
        target_idx = key_to_index[ruleKey]
        
        # Count items where the attribute at target_idx matches ruleValue
        return sum(1 for item in items if item[target_idx] == ruleValue)
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process
The problem requires checking a specific attribute of each item against `ruleValue`. 
Each item is represented as a list of three elements: `[type, color, name]`. Rather than branching via conditional checks inside the loop for each item, we can predetermine the target index corresponding to `ruleKey`:
- `"type"` corresponds to index `0`
- `"color"` corresponds to index `1`
- `"name"` corresponds to index `2`

Once the relevant index is determined in $O(1)$ time, we perform a single pass over the list of items, incrementing our count whenever `item[target_idx] == ruleValue`.

### Step-by-Step Approach
1. **Index Mapping**: Use a dictionary `key_to_index` to map the `ruleKey` string to its respective column index `(0, 1, or 2)`.
2. **Iteration & Counting**: Using a generator expression with `sum()`, iterate through each item in `items`, check if `item[target_idx] == ruleValue`, and accumulate matches.

### Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N \times L)$, where $N$ is the number of items and $L$ is the maximum length of the string being compared (constrained to $\le 10$). Since $L$ is small and constant, this operates in optimal linear time $\mathcal{O}(N)$.
- **Space Complexity**: $\mathcal{O}(1)$ auxiliary space. The index mapping is constant size and the generator expression computes the count on the fly without allocating intermediate lists.

### Common Pitfalls / Mistakes Candidates Make
1. **Inefficient Conditional Checks Inside the Loop**: Checking `if ruleKey == "type"` inside the iteration over all $N$ items introduces redundant operations. Precomputing the index outside the loop is cleaner and faster.
2. **Allocating Unnecessary Memory**: Using a list comprehension `[1 for item in items if ...]` allocates an $\mathcal{O}(N)$ array before passing it to `len()` or `sum()`. Using a generator expression keeps memory strictly $\mathcal{O}(1)$.

### Real Interview Follow-Up Questions & Answers

#### 1. What if there are millions of queries with different `ruleKey` and `ruleValue` on a static dataset?
*Answer*: Linear scan per query becomes $\mathcal{O}(Q \times N)$, which is too slow. We should pre-index the data:
- Build an inverted index / hash map for each attribute: `indices = {"type": defaultdict(int), "color": defaultdict(int), "name": defaultdict(int)}`.
- Populate frequencies in $\mathcal{O}(N)$ time.
- Answer each query in $\mathcal{O}(1)$ average time by looking up `indices[ruleKey][ruleValue]`.

#### 2. What if items arrive as a continuous, high-volume real-time stream?
*Answer*: We maintain running frequency maps using hash maps (or Redis for distributed setups). As each item arrives:
```python
counts["type"][item[0]] += 1
counts["color"][item[1]] += 1
counts["name"][item[2]] += 1
```
Any query at timestamp $T$ can return the exact match count in $\mathcal{O}(1)$. If memory is constrained and approximate counts suffice, a Count-Min Sketch or Bloom filter variant can be used.

#### 3. What if the dataset is too large to fit in memory (e.g., billions of items on disk/distributed)?
*Answer*: Use a MapReduce paradigm (or Apache Spark).
- **Map phase**: Each worker takes a partition of `items`, filters items where `item[target_idx] == ruleValue`, and outputs a local count.
- **Reduce phase**: Aggregate local counts across all partitions to produce the final result.

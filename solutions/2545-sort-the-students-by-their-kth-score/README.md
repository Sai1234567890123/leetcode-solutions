# 2545. Sort the Students by Their Kth Score

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/sort-the-students-by-their-kth-score/](https://leetcode.com/problems/sort-the-students-by-their-kth-score/)  
**Topics:** Array, Sorting, Matrix

---

## 📝 Problem Statement

There is a class with `m` students and `n` exams. You are given a **0-indexed** `m x n` integer matrix `score`, where each row represents one student and `score[i][j]` denotes the score the `ith` student got in the `jth` exam. The matrix `score` contains **distinct** integers only.

You are also given an integer `k`. Sort the students (i.e., the rows of the matrix) by their scores in the `kth` (**0-indexed**) exam from the highest to the lowest.

Return *the matrix after sorting it.*

 
Example 1:

```

**Input:** score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]], k = 2
**Output:** [[7,5,11,2],[10,6,9,1],[4,8,3,15]]
**Explanation:** In the above diagram, S denotes the student, while E denotes the exam.
- The student with index 1 scored 11 in exam 2, which is the highest score, so they got first place.
- The student with index 0 scored 9 in exam 2, which is the second highest score, so they got second place.
- The student with index 2 scored 3 in exam 2, which is the lowest score, so they got third place.

```

Example 2:

```

**Input:** score = [[3,4],[5,6]], k = 0
**Output:** [[5,6],[3,4]]
**Explanation:** In the above diagram, S denotes the student, while E denotes the exam.
- The student with index 1 scored 5 in exam 0, which is the highest score, so they got first place.
- The student with index 0 scored 3 in exam 0, which is the lowest score, so they got second place.

```

 
**Constraints:**

	- `m == score.length`

	- `n == score[i].length`

	- `1 5`

	- `score` consists of **distinct** integers.

	- `0

---

## 💻 Implementation (python3)

```py
class Solution:
    def sortTheStudents(self, score: list[list[int]], k: int) -> list[list[int]]:
        # Sort the rows in-place in descending order based on the k-th column score.
        # Python's Timsort operates on the row references, so the individual
        # row arrays are not copied or re-created, achieving optimal efficiency.
        score.sort(key=lambda row: row[k], reverse=True)
        return score
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks us to sort the rows of a 2D matrix based on the values in a specific column index `k` in descending order (highest score to lowest score).

In Python, a 2D array (`list[list[int]]`) is represented as a list of references (pointers) to 1D lists. To sort the students:
1. We only need to rearrange the references to the rows rather than deep-copying or moving the internal elements of each row.
2. By utilizing Python's built-in `sort()` method with a `key` parameter that extracts `row[k]` and setting `reverse=True`, we sort directly on the target column values in descending order.

### Step-by-Step Approach

1. Call `score.sort(key=lambda row: row[k], reverse=True)`:
   - For each row, the key function extracts the student's score in exam `k` (`row[k]`).
   - The comparison compares these scalar values in $O(1)$ time.
   - `reverse=True` ensures higher scores come first.
2. Return the mutated `score` matrix.

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(m \log m)$
  - There are $m$ rows in the matrix.
  - Python uses Timsort, which takes $\mathcal{O}(m \log m)$ comparisons in the worst case.
  - Each key extraction and integer comparison takes $\mathcal{O}(1)$ time.
  - Hence, the overall time complexity is $\mathcal{O}(m \log m)$, independent of $n$ (the number of exams).

- **Space Complexity:** $\mathcal{O}(m)$ auxiliary space
  - Timsort requires $\mathcal{O}(m)$ temporary space in the worst case to store run information and merge slices of the list.
  - If we only consider auxiliary heap memory beyond standard sorting internal buffers, it is $\mathcal{O}(1)$ extra user memory since sorting is done in-place on the existing list of row references.

---

### Common Pitfalls / Mistakes Candidates Make

1. **Copying the Entire Matrix:** Reconstructing a brand-new 2D array or copying rows unnecessarily results in $\mathcal{O}(m \cdot n)$ space complexity instead of reordering pointers in-place.
2. **Ascending vs. Descending:** Forgetting to sort in descending order (`reverse=True` or `key=lambda row: -row[k]`). Note that using `-row[k]` works for integers, but `reverse=True` is cleaner, avoids potential integer sign edge cases in other languages, and works for non-numeric/floating types.
3. **Index Out of Bounds:** Forgetting that $k$ is 0-indexed and directly represents the column index.

---

### Real Interview Follow-Up Questions

#### 1. What if scores are not distinct and we need to break ties?
- **Answer:** If we need to break ties using student ID (original row index) or another exam:
  - *Stability:* Python's Timsort is stable. If ties should retain their initial relative order, simply sorting by `key=lambda row: row[k], reverse=True` keeps the original relative ordering of tied scores.
  - *Secondary Exam Criteria:* If ties should be broken by another exam (e.g., exam $j$), we can provide a tuple key: `key=lambda row: (row[k], row[j])`.

#### 2. How would you handle this if $m$ is massive and does not fit in RAM (External Sorting)?
- **Answer:**
  - We can use **External Merge Sort**:
    1. Read chunks of rows that fit into memory, sort each chunk using the $k$-th score, and write them to temporary files on disk.
    2. Perform a multi-way merge using a min/max heap over the sorted temporary files, streaming the results directly to the output destination.

#### 3. What if we only need the top $P$ students instead of sorting all $m$ students?
- **Answer:**
  - When $P \ll m$, full sorting in $\mathcal{O}(m \log m)$ is sub-optimal.
  - We can use a min-heap of size $P$ to maintain the top $P$ scores in $\mathcal{O}(m \log P)$ time and $\mathcal{O}(P)$ space.
  - Alternatively, in an offline setting, Quickselect (`introselect`) finds the $P$-th element in $\mathcal{O}(m)$ average time, followed by sorting only the top $P$ elements in $\mathcal{O}(P \log P)$ time.

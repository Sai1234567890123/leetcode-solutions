# 3516. Find Closest Person

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/find-closest-person/](https://leetcode.com/problems/find-closest-person/)  
**Topics:** Math

---

## 📝 Problem Statement

You are given three integers x, y, and z, representing the positions of three people on a number line:

	x is the position of Person 1.
	y is the position of Person 2.
	z is the position of Person 3, who does **not** move.

Both Person 1 and Person 2 move toward Person 3 at the **same** speed.

Determine which person reaches Person 3 **first**:

	Return 1 if Person 1 arrives first.
	Return 2 if Person 2 arrives first.
	Return 0 if both arrive at the **same** time.

Return the result accordingly.

 
Example 1:

**Input:** x = 2, y = 7, z = 4

**Output:** 1

**Explanation:**

	Person 1 is at position 2 and can reach Person 3 (at position 4) in 2 steps.
	Person 2 is at position 7 and can reach Person 3 in 3 steps.

Since Person 1 reaches Person 3 first, the output is 1.

Example 2:

**Input:** x = 2, y = 5, z = 6

**Output:** 2

**Explanation:**

	Person 1 is at position 2 and can reach Person 3 (at position 6) in 4 steps.
	Person 2 is at position 5 and can reach Person 3 in 1 step.

Since Person 2 reaches Person 3 first, the output is 2.

Example 3:

**Input:** x = 1, y = 5, z = 3

**Output:** 0

**Explanation:**

	Person 1 is at position 1 and can reach Person 3 (at position 3) in 2 steps.
	Person 2 is at position 5 and can reach Person 3 in 2 steps.

Since both Person 1 and Person 2 reach Person 3 at the same time, the output is 0.

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        # Calculate the absolute distance from each person to Person 3 (at position z)
        dist1 = abs(x - z)
        dist2 = abs(y - z)
        
        # Since both move at the same speed, shorter distance means earlier arrival
        if dist1 < dist2:
            return 1
        elif dist2 < dist1:
            return 2
        else:
            return 0
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks which person (Person 1 at position `x` or Person 2 at position `y`) reaches Person 3 (at fixed position `z`) first, assuming both move at the exact same constant speed.

From basic kinematics:
$$\text{Time} = \frac{\text{Distance}}{\text{Speed}}$$

Because both individuals move at the same speed, the arrival time is directly proportional to the distance each person must travel. On a one-dimensional coordinate line, the distance between any two positions $A$ and $B$ is given by the absolute difference $|A - B|$:
- Person 1's distance: $|x - z|$
- Person 2's distance: $|y - z|$

Comparing these two distances gives the answer directly:
- If $|x - z| < |y - z|$, Person 1 arrives first $\implies$ return `1`.
- If $|y - z| < |x - z|$, Person 2 arrives first $\implies$ return `2`.
- If $|x - z| = |y - z|$, both arrive at the same time $\implies$ return `0`.

---

### Step-by-Step Approach

1. Compute `dist1 = abs(x - z)`.
2. Compute `dist2 = abs(y - z)`.
3. Use conditional statements to compare `dist1` and `dist2` and return `1`, `2`, or `0` accordingly.

---

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(1)$ - We perform basic subtraction, absolute value calculation, and comparison operations, all of which run in constant time.
- **Space Complexity:** $\mathcal{O}(1)$ - Only a couple of scalar variables are maintained, requiring $\mathcal{O}(1)$ auxiliary memory.

---

### Common Pitfalls / Mistakes Candidates Make

1. **Forgetting Absolute Value:** Doing `(x - z)` and `(y - z)` directly without taking the absolute value can lead to negative distances if a person is positioned to the left of `z`.
2. **Speed Mismatch Assumptions:** Overcomplicating the problem by trying to simulate the movement step-by-step or frame-by-frame instead of directly calculating Euclidean/Manhattan distance on 1D space.

---

### Real Interview Follow-Up Questions & Answers

#### 1. What if people move at different speeds?
**Answer:** If Person 1 moves at speed $v_1$ and Person 2 at $v_2$, their arrival times are $t_1 = \frac{|x - z|}{v_1}$ and $t_2 = \frac{|y - z|}{v_2}$. To avoid floating-point inaccuracies, compare cross-multiplied integers:
$$|x - z| \cdot v_2 \quad \text{vs} \quad |y - z| \cdot v_1$$

#### 2. How does this scale to 2D/3D space?
**Answer:** In 2D or 3D space, distance can be measured via Euclidean distance ($d = \sqrt{\Delta x^2 + \Delta y^2}$) or Manhattan distance ($d = |\Delta x| + |\Delta y|$). If comparing Euclidean distances, we compare the squared Euclidean distances ($\Delta x^2 + \Delta y^2$) directly to stay entirely in integer arithmetic and avoid expensive square root operations.

#### 3. How would you handle $N$ people moving towards Person 3?
**Answer:** 
- If $N$ is static and small-to-moderate, a single pass ($\mathcal{O}(N)$) tracking the minimum distance and all candidate indices handles ties and finding the winner.
- If queries arrive continuously (e.g., streaming queries for nearest neighbor), a spatial data structure like a Binary Search Tree (for 1D) or a KD-Tree / Vantage-Point Tree (for $\ge 2\text{D}$) allows $\mathcal{O}(\log N)$ nearest-neighbor lookups.

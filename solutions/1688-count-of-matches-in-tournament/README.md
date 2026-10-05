# 1688. Count of Matches in Tournament

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/count-of-matches-in-tournament/](https://leetcode.com/problems/count-of-matches-in-tournament/)  
**Topics:** Math, Simulation

---

## 📝 Problem Statement

You are given an integer `n`, the number of teams in a tournament that has strange rules:

	- If the current number of teams is **even**, each team gets paired with another team. A total of `n / 2` matches are played, and `n / 2` teams advance to the next round.

	- If the current number of teams is **odd**, one team randomly advances in the tournament, and the rest gets paired. A total of `(n - 1) / 2` matches are played, and `(n - 1) / 2 + 1` teams advance to the next round.

Return *the number of matches played in the tournament until a winner is decided.*

 
Example 1:

```

**Input:** n = 7
**Output:** 6
**Explanation:** Details of the tournament: 
- 1st Round: Teams = 7, Matches = 3, and 4 teams advance.
- 2nd Round: Teams = 4, Matches = 2, and 2 teams advance.
- 3rd Round: Teams = 2, Matches = 1, and 1 team is declared the winner.
Total number of matches = 3 + 2 + 1 = 6.

```

Example 2:

```

**Input:** n = 14
**Output:** 13
**Explanation:** Details of the tournament:
- 1st Round: Teams = 14, Matches = 7, and 7 teams advance.
- 2nd Round: Teams = 7, Matches = 3, and 4 teams advance.
- 3rd Round: Teams = 4, Matches = 2, and 2 teams advance.
- 4th Round: Teams = 2, Matches = 1, and 1 team is declared the winner.
Total number of matches = 7 + 3 + 2 + 1 = 13.

```

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def numberOfMatches(self, n: int) -> int:
        """
        In a single-elimination tournament:
        - Each match eliminates exactly 1 team.
        - To determine 1 winner from n teams, exactly n - 1 teams must be eliminated.
        - Therefore, exactly n - 1 matches must be played.
        """
        return n - 1
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

At first glance, the problem suggests a simulation approach:
- If $n$ is even, simulate $\frac{n}{2}$ matches and advance $\frac{n}{2}$ teams.
- If $n$ is odd, simulate $\frac{n - 1}{2}$ matches and advance $\frac{n - 1}{2} + 1$ teams.
- Continue in a loop until $n = 1$, which runs in $O(\log n)$ time.

However, recognizing the fundamental invariant of a knockout/elimination tournament allows for an $O(1)$ solution:
1. Every single match eliminates **exactly one** team.
2. The tournament starts with $n$ teams and ends when there is **exactly one** winner left.
3. Therefore, exactly $n - 1$ teams must be eliminated.
4. Since each match produces one elimination, the total number of matches must always equal **$n - 1$**, regardless of the pairing scheme or byes.

### Step-by-Step Approach

1. Return `n - 1`.

### Complexity Analysis

- **Time Complexity:** $O(1)$ — A single arithmetic subtraction operation.
- **Space Complexity:** $O(1)$ — No auxiliary data structures or call stack frames are used.

---

### Common Pitfalls / Mistakes Candidates Make

1. **Over-engineering with Simulation:** Many candidates immediately write a `while n > 1` loop. While accepted, in a senior/principal interview, failing to recognize the mathematical invariant ($n - 1$) indicates a tendency to jump into coding without analyzing the broader problem structure.
2. **Off-by-One / Parity Errors in Simulation:** If implementing the simulation approach, candidates frequently make integer division mistakes (e.g., using `/` instead of `//` in Python or miscalculating the number of advancing teams for odd numbers).
3. **Edge Case $n = 1$:** Missing the base case where $n = 1$ requires $0$ matches. $n - 1 = 0$ naturally handles this.

---

### Real Interview Follow-Up Questions

#### 1. What if each match eliminates $k$ teams instead of $1$ (e.g., a battle royale game where $m$ players enter and $m - k$ survive)?
**Answer:** 
If each match eliminates $k$ teams, and we still need to reach $1$ winner, we need to eliminate $n - 1$ teams. If each match eliminates a fixed $k$ teams, the number of matches would be $\frac{n - 1}{k}$ (assuming $n - 1$ is divisible by $k$). If leftover teams get partial matches or byes, we floor/ceil appropriately, but tracking total eliminations remains the core invariant.

#### 2. What if it is a Double Elimination tournament?
**Answer:** 
In a double-elimination tournament:
- Every team except the winner must lose twice.
- $n - 1$ teams are eliminated by losing 2 matches each, accounting for $2(n - 1)$ losses.
- The winner can have either 0 or 1 loss.
- Thus, the tournament will take either $2n - 2$ or $2n - 1$ matches depending on whether the finalist from the losers bracket resets the bracket.

#### 3. How would you solve this if $n$ is an extremely large number (e.g., $n > 2^{64}$)?
**Answer:**
In Python, integers have arbitrary precision, so `n - 1` still works seamlessly. In languages with fixed-width integers like C++ or Java (`uint64_t` or `long`), we would need to use `BigInteger` / string representations to prevent overflow, although `n - 1` itself only requires a single subtraction and does not risk overflow for $n \ge 1$.

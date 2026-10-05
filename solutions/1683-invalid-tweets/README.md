# 1683. Invalid Tweets

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/invalid-tweets/](https://leetcode.com/problems/invalid-tweets/)  
**Topics:** Database

---

## 📝 Problem Statement

Table: `Tweets`

```

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| tweet_id       | int     |
| content        | varchar |
+----------------+---------+
tweet_id is the primary key (column with unique values) for this table.
content consists of alphanumeric characters, '!', or ' ' and no other special characters.
This table contains all the tweets in a social media app.

```

 

Write a solution to find the IDs of the invalid tweets. The tweet is invalid if the number of characters used in the content of the tweet is **strictly greater** than `15`.

Return the result table in **any order**.

The result format is in the following example.

 
Example 1:

```

**Input:** 
Tweets table:
+----------+-----------------------------------+
| tweet_id | content                           |
+----------+-----------------------------------+
| 1        | Let us Code                       |
| 2        | More than fifteen chars are here! |
+----------+-----------------------------------+
**Output:** 
+----------+
| tweet_id |
+----------+
| 2        |
+----------+
**Explanation:** 
Tweet 1 has length = 11. It is a valid tweet.
Tweet 2 has length = 33. It is an invalid tweet.

```

---

## 💻 Implementation (python3)

```py
SELECT 
    tweet_id
FROM 
    Tweets
WHERE 
    CHAR_LENGTH(content) > 15;
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks for tweets where the number of characters exceeds $15$. 

In SQL (specifically MySQL), there are two primary string length functions:
1. `LENGTH(str)`: Returns the length of the string in **bytes**.
2. `CHAR_LENGTH(str)` (or `CHARACTER_LENGTH(str)`): Returns the length of the string measured in **characters**.

Although the problem description states that `content` contains only alphanumeric characters, spaces, and exclamation marks (which all use 1 byte in standard encodings like UTF-8), using `CHAR_LENGTH()` is the production-grade choice. In real-world social media applications where tweets contain multibyte characters (such as emojis or international character sets like Chinese, Japanese, or Arabic), `LENGTH()` would return the byte count rather than character count, causing false positives.

### Step-by-Step Approach

1. **Select Column**: Project only `tweet_id`.
2. **Filter Condition**: Use `CHAR_LENGTH(content) > 15` in the `WHERE` clause to filter out tweets that have $15$ or fewer characters.

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \times L)$, where $N$ is the number of rows in the `Tweets` table and $L$ is the average length of `content`. A full table scan is performed, and `CHAR_LENGTH` runs in time proportional to the length of each string.
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary space (excluding the output table).

### Common Pitfalls / Mistakes

1. **`LENGTH()` vs. `CHAR_LENGTH()`**: Using `LENGTH()` can lead to bugs with multi-byte UTF-8 encodings (e.g., an emoji like 🚀 takes 4 bytes in `utf8mb4`, which would count as 4 with `LENGTH()`, but only 1 with `CHAR_LENGTH()`).
2. **Off-by-one errors**: The condition requires *strictly greater than 15* (`> 15`), not greater than or equal to (`>= 15`).
3. **Handling `NULL` values**: If `content` could be `NULL`, `CHAR_LENGTH(NULL)` evaluates to `NULL`, which is treated as false in a `WHERE` clause. If invalid meant null as well, an explicit `OR content IS NULL` would be required, though here `content` is given as standard text.

### Real Interview Follow-Up Questions

#### 1. What if the table contains billions of tweets and this query runs frequently?
- **Answer:** Applying a function like `CHAR_LENGTH(content)` in the `WHERE` clause prevents MySQL from utilizing a standard B-Tree index on `content` (it is not SARGable).
- **Optimization:** 
  1. Add a generated/virtual column for character length:
     ```sql
     ALTER TABLE Tweets ADD COLUMN content_len INT GENERATED ALWAYS AS (CHAR_LENGTH(content)) STORED;
     CREATE INDEX idx_content_len ON Tweets (content_len);
     ```
  2. Query using: `SELECT tweet_id FROM Tweets WHERE content_len > 15;`

#### 2. How should this constraint be enforced at scale before reaching the database?
- **Answer:** Such validation should ideally be enforced:
  1. At the API Gateway / Application layer (rejecting invalid payloads immediately with HTTP 400).
  2. At the database layer using a `CHECK` constraint:
     ```sql
     ALTER TABLE Tweets ADD CONSTRAINT chk_tweet_length CHECK (CHAR_LENGTH(content) <= 15);
     ```

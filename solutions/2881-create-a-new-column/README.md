# 2881. Create a New Column

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/create-a-new-column/](https://leetcode.com/problems/create-a-new-column/)  
**Topics:** 

---

## 📝 Problem Statement

```

DataFrame `employees`
+-------------+--------+
| Column Name | Type.  |
+-------------+--------+
| name        | object |
| salary      | int.   |
+-------------+--------+

```

A company plans to provide its employees with a bonus.

Write a solution to create a new column name `bonus` that contains the **doubled values** of the `salary` column.

The result format is in the following example.

 
Example 1:

```

**Input:**
DataFrame employees
+---------+--------+
| name    | salary |
+---------+--------+
| Piper   | 4548   |
| Grace   | 28150  |
| Georgia | 1103   |
| Willow  | 6593   |
| Finn    | 74576  |
| Thomas  | 24433  |
+---------+--------+
**Output:**
+---------+--------+--------+
| name    | salary | bonus  |
+---------+--------+--------+
| Piper   | 4548   | 9096   |
| Grace   | 28150  | 56300  |
| Georgia | 1103   | 2206   |
| Willow  | 6593   | 13186  |
| Finn    | 74576  | 149152 |
| Thomas  | 24433  | 48866  |
+---------+--------+--------+
**Explanation:** 
A new column bonus is created by doubling the value in the column salary.
```

---

## 💻 Implementation (python3)

```py
import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    # Create a new column named 'bonus'
    # This column's values are calculated by taking the 'salary' column
    # and multiplying each element by 2.
    # Pandas automatically handles this as a vectorized operation,
    # applying the multiplication to every row efficiently.
    employees['bonus'] = employees['salary'] * 2
    
    # Return the modified DataFrame which now includes the 'bonus' column.
    return employees
```

---

## 💡 Solution, Complexity & Interview Analysis

Detailed explanation not extracted.

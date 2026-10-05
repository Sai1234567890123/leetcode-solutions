# 2879. Display the First Three Rows

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/display-the-first-three-rows/](https://leetcode.com/problems/display-the-first-three-rows/)  
**Topics:** 

---

## 📝 Problem Statement

```

DataFrame: `employees`
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| employee_id | int    |
| name        | object |
| department  | object |
| salary      | int    |
+-------------+--------+

```

Write a solution to display the **first `3` **rows** **of this DataFrame.

 
Example 1:

```

Input:
DataFrame employees
+-------------+-----------+-----------------------+--------+
| employee_id | name      | department            | salary |
+-------------+-----------+-----------------------+--------+
| 3           | Bob       | Operations            | 48675  |
| 90          | Alice     | Sales                 | 11096  |
| 9           | Tatiana   | Engineering           | 33805  |
| 60          | Annabelle | InformationTechnology | 37678  |
| 49          | Jonathan  | HumanResources        | 23793  |
| 43          | Khaled    | Administration        | 40454  |
+-------------+-----------+-----------------------+--------+
**Output:**
+-------------+---------+-------------+--------+
| employee_id | name    | department  | salary |
+-------------+---------+-------------+--------+
| 3           | Bob     | Operations  | 48675  |
| 90          | Alice   | Sales       | 11096  |
| 9           | Tatiana | Engineering | 33805  |
+-------------+---------+-------------+--------+
**Explanation:** 
Only the first 3 rows are displayed.
```

---

## 💻 Implementation (python3)

```py
import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    # Use the .head() method to select the first N rows of a DataFrame.
    # When N=3, it returns the first 3 rows.
    # If the DataFrame has fewer than 3 rows, it will return all available rows.
    return employees.head(3)
```

---

## 💡 Solution, Complexity & Interview Analysis

Detailed explanation not extracted.

# 3668. Restore Finishing Order

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/restore-finishing-order/](https://leetcode.com/problems/restore-finishing-order/)  
**Topics:** Array, Hash Table

---

## 📝 Problem Statement

You are given an integer array `order` of length `n` and an integer array `friends`.

	- `order` contains every integer from 1 to `n` **exactly once**, representing the IDs of the participants of a race in their **finishing** order.

	- `friends` contains the IDs of your friends in the race **sorted** in strictly increasing order. Each ID in friends is guaranteed to appear in the `order` array.

Return an array containing your friends' IDs in their **finishing** order.

 
Example 1:

**Input:** order = [3,1,2,5,4], friends = [1,3,4]

**Output:** [3,1,4]

**Explanation:**

The finishing order is `[**3**, **1**, 2, 5, **4**]`. Therefore, the finishing order of your friends is `[3, 1, 4]`.

Example 2:

**Input:** order = [1,4,5,3,2], friends = [2,5]

**Output:** [5,2]

**Explanation:**

The finishing order is `[1, 4, **5**, 3, **2**]`. Therefore, the finishing order of your friends is `[5, 2]`.

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
from typing import List

class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        # Step 1: Create a hash set (or 'set' in Python) from the 'friends' list.
        # This allows for O(1) average time complexity for checking if a participant ID
        # is one of our friends. The 'friends' list being sorted is not directly
        # leveraged here, as set construction and lookup don't depend on input order.
        friend_set = set(friends)
        
        # Step 2: Initialize an empty list to store the IDs of friends in their
        # finishing order. This list will be our final result.
        result = []
        
        # Step 3: Iterate through the 'order' array. This array represents the
        # participants in their exact finishing sequence.
        for participant_id in order:
            # Step 4: For each participant in the finishing order, check if their ID
            # is present in our 'friend_set'.
            if participant_id in friend_set:
                # If the participant is found in the 'friend_set', it means they are
                # one of our friends. We add their ID to our 'result' list.
                # By iterating through 'order' and appending, we naturally preserve
                # the relative finishing order of our friends.
                result.append(participant_id)
                
        # Step 5: After checking all participants in the 'order' array, the 'result'
        # list will contain all our friends' IDs in their correct finishing order.
        return result
```

---

## 💡 Solution, Complexity & Interview Analysis

Detailed explanation not extracted.

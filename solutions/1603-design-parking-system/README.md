# 1603. Design Parking System

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/design-parking-system/](https://leetcode.com/problems/design-parking-system/)  
**Topics:** Design, Simulation, Counting

---

## 📝 Problem Statement

Design a parking system for a parking lot. The parking lot has three kinds of parking spaces: big, medium, and small, with a fixed number of slots for each size.

Implement the `ParkingSystem` class:

	- `ParkingSystem(int big, int medium, int small)` Initializes object of the `ParkingSystem` class. The number of slots for each parking space are given as part of the constructor.

	- `bool addCar(int carType)` Checks whether there is a parking space of `carType` for the car that wants to get into the parking lot. `carType` can be of three kinds: big, medium, or small, which are represented by `1`, `2`, and `3` respectively. **A car can only park in a parking space of its **`carType`. If there is no space available, return `false`, else park the car in that size space and return `true`.

 
Example 1:

```

**Input**
["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
[[1, 1, 0], [1], [2], [3], [1]]
**Output**
[null, true, true, false, false]

**Explanation**
ParkingSystem parkingSystem = new ParkingSystem(1, 1, 0);
parkingSystem.addCar(1); // return true because there is 1 available slot for a big car
parkingSystem.addCar(2); // return true because there is 1 available slot for a medium car
parkingSystem.addCar(3); // return false because there is no available slot for a small car
parkingSystem.addCar(1); // return false because there is no available slot for a big car. It is already occupied.

```

 
**Constraints:**

	- `0

---

## 💻 Implementation (python3)

```py
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        """
        Initializes the parking system with the given number of slots
        for each car type.
        Index 1: Big
        Index 2: Medium
        Index 3: Small
        Using a 1-indexed list avoids off-by-one arithmetic in addCar.
        """
        self.available_slots = [0, big, medium, small]

    def addCar(self, carType: int) -> bool:
        """
        Checks if a slot is available for the given carType.
        If available, decrements the slot count and returns True.
        Otherwise, returns False.
        """
        if self.available_slots[carType] > 0:
            self.available_slots[carType] -= 1
            return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem requires tracking the remaining capacity for three distinct types of parking spaces:
- Big (`carType = 1`)
- Medium (`carType = 2`)
- Small (`carType = 3`)

Whenever a car of a particular `carType` attempts to enter:
1. We check if the remaining slot count for that `carType` is strictly greater than 0.
2. If so, we decrement the slot count by 1 and return `True`.
3. If the slot count is 0, no space is available, so we return `False`.

Instead of using three separate variables or a hash map, we can use a 1-indexed array of size 4: `[0, big, medium, small]`. This allows direct indexing using `carType` without offset calculations (`carType - 1`), yielding concise, branchless, and cache-friendly code.

---

### Step-by-Step Approach

1. **Initialization (`__init__`)**:
   - Store the counts in a list `self.available_slots = [0, big, medium, small]`.
2. **Adding a Car (`addCar`)**:
   - Access `self.available_slots[carType]`.
   - If greater than 0, decrement by 1 and return `True`.
   - Otherwise, return `False`.

---

### Complexity Analysis

- **Time Complexity:**
  - `__init__`: $O(1)$ — initializing a fixed-size list of 4 integers.
  - `addCar`: $O(1)$ — direct array index lookup, comparison, and decrement.
- **Space Complexity:**
  - Overall Auxiliary Space: $O(1)$ — constant storage for a 4-element list regardless of the number of operations.

---

### Common Pitfalls / Mistakes

- **0-indexing vs 1-indexing**: Forgetting that `carType` starts from 1, leading to `IndexError` if using a 3-element list without doing `carType - 1`.
- **Negative slot counts**: Failing to check whether capacity is greater than 0 before decrementing, leading to negative remaining spaces.
- **Over-engineering**: Creating full OOP class hierarchies (`Vehicle`, `ParkingSlot`, etc.) for an algorithmic task when a lightweight, performant representation is desired. (Always clarify whether the interviewer wants a high-level system design model or high-performance algorithmic primitives).

---

### Real Interview Follow-Up Questions & Answers

#### 1. Concurrency / Multi-threading:
- **Question**: "What if multiple cars enter simultaneously across multiple entrance gates in a multi-threaded environment?"
- **Answer**: 
  - The check-then-decrement operation is not atomic (race condition). Two threads checking a remaining count of 1 at the same time could both park, resulting in overbooking.
  - **Solution in Python**: Use `threading.Lock()` or an array of locks (one per `carType`) so that only one thread can query and update a given car type at a time.
  - **Lock-free / Low-level**: In languages like C++ or Java, use atomic types (`std::atomic<int>` / `AtomicInteger`) and compare-and-swap operations (`compare_exchange_weak`) or fetch-and-subtract with non-negative bounds checking.

#### 2. Releasing Parking Slots:
- **Question**: "How would you support a `removeCar(carType)` method?"
- **Answer**:
  - Store the initial capacities: `self.max_capacity = [0, big, medium, small]`.
  - When `removeCar(carType)` is invoked, check `if self.available_slots[carType] < self.max_capacity[carType]: self.available_slots[carType] += 1; return True`.

#### 3. Flexible Parking Policy (Subsuming smaller cars):
- **Question**: "What if a smaller car is allowed to park in a larger spot if its designated size is full?"
- **Answer**:
  - If a small car (`3`) arrives and small spots are full, it can check medium (`2`), then big (`1`).
  - Implementation: Loop from `carType` down to 1:
    ```python
    for slot_type in range(carType, 0, -1):
        if self.available_slots[slot_type] > 0:
            self.available_slots[slot_type] -= 1
            return True
    return False
    ```

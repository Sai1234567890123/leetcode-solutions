class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        # Initialize three empty lists to categorize elements based on their comparison with the pivot.
        # 'less_than_pivot' will store elements smaller than the pivot.
        # 'equal_to_pivot' will store elements equal to the pivot.
        # 'greater_than_pivot' will store elements larger than the pivot.
        less_than_pivot = []
        equal_to_pivot = []
        greater_than_pivot = []

        # Iterate through the input array 'nums' exactly once.
        # This single pass is crucial for maintaining the relative order of elements
        # within each of the three categories (less, equal, greater).
        for num in nums:
            if num < pivot:
                less_than_pivot.append(num) # Append to the list for elements less than pivot
            elif num == pivot:
                equal_to_pivot.append(num) # Append to the list for elements equal to pivot
            else: # num > pivot
                greater_than_pivot.append(num) # Append to the list for elements greater than pivot
        
        # Concatenate the three lists in the specified order:
        # 1. All elements less than the pivot.
        # 2. All elements equal to the pivot.
        # 3. All elements greater than the pivot.
        # This concatenation forms the final rearranged array.
        return less_than_pivot + equal_to_pivot + greater_than_pivot

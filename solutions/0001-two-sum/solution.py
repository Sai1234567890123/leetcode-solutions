class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Create a hash map (dictionary in Python) to store numbers and their indices.
        # The key will be the number, and the value will be its index.
        num_map = {} 

        # Iterate through the array with both index and value using enumerate.
        for i, num in enumerate(nums):
            # Calculate the complement needed to reach the target.
            # If 'num' is one of the numbers, 'complement' is the other.
            complement = target - num

            # Check if the complement already exists in our hash map.
            # If it does, we've found the two numbers that sum up to the target.
            if complement in num_map:
                # Return the index of the complement (which was stored earlier)
                # and the current index 'i'.
                return [num_map[complement], i]
            
            # If the complement is not found, add the current number and its index to the hash map.
            # This makes the current 'num' available as a potential complement for subsequent numbers.
            num_map[num] = i
        
        # According to the problem statement, there will always be exactly one solution.
        # Therefore, this line should theoretically never be reached.
        # It's included for completeness, though the problem guarantees a return within the loop.
        return []

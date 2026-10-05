class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        # Precompute the current maximum number of candies any kid has.
        max_candies = max(candies)
        
        # A kid can have the greatest number of candies if their current candies + extraCandies >= max_candies.
        # Alternatively: candies[i] >= max_candies - extraCandies
        threshold = max_candies - extraCandies
        
        # Construct the result list using a list comprehension.
        return [candy >= threshold for candy in candies]

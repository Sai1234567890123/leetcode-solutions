class Solution:
    def stableMountains(self, height: list[int], threshold: int) -> list[int]:
        # Mountain 0 can never be stable because there is no mountain before it.
        # Check each mountain from index 1 to n - 1:
        # Mountain i is stable if height[i - 1] > threshold.
        return [i for i in range(1, len(height)) if height[i - 1] > threshold]

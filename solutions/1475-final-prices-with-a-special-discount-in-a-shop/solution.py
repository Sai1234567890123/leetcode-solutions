class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        # Using a monotonic increasing stack to track indices of items
        # waiting for their next smaller or equal discount element.
        stack = []
        ans = prices[:]
        
        for i, price in enumerate(prices):
            # Resolve discounts for all pending items in the stack that are >= current price
            while stack and prices[stack[-1]] >= price:
                prev_idx = stack.pop()
                ans[prev_idx] -= price
            
            stack.append(i)
            
        return ans

class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        """
        Calculates the maximum wealth among all customers.
        Each row represents a customer's accounts across different banks.
        """
        # Use a generator expression inside max() to maintain O(1) auxiliary space
        return max(sum(customer_accounts) for customer_accounts in accounts)

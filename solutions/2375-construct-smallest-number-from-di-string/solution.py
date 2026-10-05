class Solution:
    def smallestNumber(self, pattern: str) -> str:
        """
        Constructs the lexicographically smallest number matching the DI pattern
        using a stack-based greedy approach.
        """
        result = []
        stack = []
        n = len(pattern)

        # We need to place digits 1 through n + 1
        for i in range(n + 1):
            # Push the next smallest available digit (i + 1)
            stack.append(str(i + 1))

            # Whenever we hit an 'I' or reach the end of the pattern,
            # we reverse the accumulated decreasing sequence by popping from the stack.
            if i == n or pattern[i] == 'I':
                while stack:
                    result.append(stack.pop())

        return "".join(result)

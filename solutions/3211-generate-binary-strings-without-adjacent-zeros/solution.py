class Solution:
    def validStrings(self, n: int) -> list[str]:
        result: list[str] = []
        path: list[str] = []

        def backtrack(index: int) -> None:
            # Base case: reached the required string length
            if index == n:
                result.append("".join(path))
                return

            # Option 1: We can always append '1'
            path.append('1')
            backtrack(index + 1)
            path.pop()

            # Option 2: We can append '0' only if the preceding character is not '0'
            # (or if this is the first character being placed)
            if not path or path[-1] != '0':
                path.append('0')
                backtrack(index + 1)
                path.pop()

        backtrack(0)
        return result

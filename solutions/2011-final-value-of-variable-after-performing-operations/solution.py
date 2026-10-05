class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        # Initialize the variable X to 0, as per the problem description.
        x = 0
        
        # Iterate through each operation string in the input list.
        for op in operations:
            # The problem states there are only four types of operations:
            # "++X", "X++" (increment) and "--X", "X--" (decrement).
            #
            # A key observation is that all increment operations ("++X", "X++")
            # contain a '+' character, and all decrement operations ("--X", "X--")
            # contain a '-' character.
            #
            # Therefore, we can simply check for the presence of '+' to determine
            # if the operation is an increment. If '+' is not present, it must be
            # a decrement.
            if '+' in op:
                # If the operation string contains '+', it's an increment.
                x += 1
            else:
                # Otherwise (it must contain '-'), it's a decrement.
                x -= 1
                
        # After processing all operations, return the final value of X.
        return x

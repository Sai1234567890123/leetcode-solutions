class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        # Initialize an array to store the frequency of each digit (0-9).
        # The index represents the digit, and the value represents its frequency.
        # This array has a fixed size of 10, making space complexity O(1).
        counts = [0] * 10

        # Use a temporary variable to extract digits without modifying the original 'n'.
        # The problem constraints state 1 <= n <= 10^9, so n will always be positive.
        # This loop will run at least once (e.g., for n=1, it runs once; for n=122, it runs thrice).
        temp_n = n
        while temp_n > 0:
            # Get the last digit of temp_n using the modulo operator.
            digit = temp_n % 10
            
            # Increment the frequency count for this digit.
            counts[digit] += 1
            
            # Remove the last digit from temp_n using integer division to process the next digit.
            temp_n //= 10

        # Calculate the total score based on the frequencies.
        total_score = 0
        # Iterate through all possible digits from 0 to 9.
        for d in range(10):
            # If the digit 'd' appeared in 'n' (i.e., its frequency is greater than 0),
            # add its contribution to the total score.
            if counts[d] > 0:
                # The contribution for a digit 'd' is d multiplied by its frequency (d * freq(d)).
                total_score += d * counts[d]
        
        # Return the final calculated score.
        return total_score

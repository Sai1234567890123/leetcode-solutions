class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        n = len(boxes)
        ans = [0] * n
        
        # Pass 1: Left to right
        # Accumulate operations needed to bring all balls to the left of i into box i
        balls_count = 0
        running_ops = 0
        for i in range(n):
            ans[i] += running_ops
            balls_count += int(boxes[i])
            running_ops += balls_count
            
        # Pass 2: Right to left
        # Accumulate operations needed to bring all balls to the right of i into box i
        balls_count = 0
        running_ops = 0
        for i in range(n - 1, -1, -1):
            ans[i] += running_ops
            balls_count += int(boxes[i])
            running_ops += balls_count
            
        return ans

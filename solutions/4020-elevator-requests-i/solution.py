class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        total_time = 0
        current_floor = 0
        
        # Traverse each requested floor in order
        for target_floor in requests:
            # Add time required to travel to the next floor
            total_time += abs(target_floor - current_floor)
            # Update current floor to the new position
            current_floor = target_floor
            
        return total_time

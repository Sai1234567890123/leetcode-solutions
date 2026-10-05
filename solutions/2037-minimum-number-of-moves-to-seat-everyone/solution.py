class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        """
        Calculates the minimum moves required to seat all students.
        
        Using the greedy property (Monge property / 1D optimal transport):
        Matching the i-th smallest student position with the i-th smallest seat position
        guarantees the minimum total displacement without crossings.
        """
        # Sort both lists in non-decreasing order
        seats.sort()
        students.sort()
        
        # Sum the absolute differences between matched pairs
        return sum(abs(seat - student) for seat, student in zip(seats, students))

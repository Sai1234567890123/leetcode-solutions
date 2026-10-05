class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        """
        Finds the highest altitude reached during the trip.
        The trip starts at altitude 0.
        """
        current_altitude = 0
        max_altitude = 0

        for net_change in gain:
            current_altitude += net_change
            if current_altitude > max_altitude:
                max_altitude = current_altitude

        return max_altitude

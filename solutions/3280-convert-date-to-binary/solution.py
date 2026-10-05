class Solution:
    def convertDateToBinary(self, date: str) -> str:
        # Split the date string by '-' into [year, month, day]
        # Convert each segment to an integer, format it as a binary string without prefix,
        # and join them back with '-'
        return "-".join(f"{int(part):b}" for part in date.split("-"))

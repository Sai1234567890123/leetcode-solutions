class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        total_beams = 0
        prev_row_count = 0

        for row in bank:
            # Count the number of security devices ('1') in the current row
            curr_row_count = row.count('1')

            # If there are no devices in this row, beams pass through uninterrupted
            if curr_row_count == 0:
                continue

            # Every device in the previous valid row connects to every device in this row
            total_beams += prev_row_count * curr_row_count
            
            # Update the previous valid row device count
            prev_row_count = curr_row_count

        return total_beams

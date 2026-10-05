class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        """
        Sorts the array of names based on the corresponding heights in descending order.
        
        Args:
            names: list[str] - Names of the people.
            heights: list[int] - Distinct heights corresponding to each person.
            
        Returns:
            list[str] - Names sorted in descending order of heights.
        """
        # Pair each height with its corresponding name, sort in reverse (descending) order by height,
        # and extract only the names.
        return [name for _, name in sorted(zip(heights, names), reverse=True)]

class Solution:
    def defangIPaddr(self, address: str) -> str:
        # The problem requires replacing every period "." in the IP address with "[.]".
        # Python's built-in string `replace()` method is the most straightforward,
        # efficient, and Pythonic way to achieve this.
        # It takes two arguments: the substring to find, and the substring to replace it with.
        # It returns a new string with all occurrences of the old substring replaced.
        return address.replace(".", "[.]")

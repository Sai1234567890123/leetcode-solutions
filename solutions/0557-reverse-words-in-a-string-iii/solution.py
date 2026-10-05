class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string by single space delimiter into individual words,
        # reverse each word using slicing, and join them back with spaces.
        return ' '.join(word[::-1] for word in s.split(' '))

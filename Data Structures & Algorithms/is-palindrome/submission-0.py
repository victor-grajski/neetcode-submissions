class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lower = s.lower()
        s_alnum = "".join(char for char in s_lower if char.isalnum())
        return s_alnum == s_alnum[::-1]
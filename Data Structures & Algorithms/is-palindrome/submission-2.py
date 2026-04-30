class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_alnum = ""
        for i, c in enumerate(s.lower()):
            if c.isalnum():
                s_alnum += c
        return s_alnum == s_alnum[::-1]
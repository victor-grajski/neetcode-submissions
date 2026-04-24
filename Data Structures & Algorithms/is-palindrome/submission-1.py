class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lower = s.lower()
        s_alnum = "".join(char for char in s_lower if char.isalnum())

        right = len(s_alnum) - 1
        for i in range(len(s_alnum)):
            if s_alnum[i] != s_alnum[right]:
                return False
            right -= 1
        return True
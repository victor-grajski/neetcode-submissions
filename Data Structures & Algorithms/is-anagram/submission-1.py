class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_seen = {}
        t_seen = {}

        for i, character in enumerate(sorted(s)):
            if character in s_seen:
                s_seen[character] += 1
            else:
                s_seen[character] = 1

        for i, character in enumerate(sorted(t)):
            if character in t_seen:
                t_seen[character] += 1
            else:
                t_seen[character] = 1

        return s_seen == t_seen
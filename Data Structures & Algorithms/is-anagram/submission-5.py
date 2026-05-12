class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_seen = defaultdict(int)
        t_seen = defaultdict(int)

        for c in s:
            s_seen[c] += 1
        for c in t:
            t_seen[c] += 1
        return s_seen == t_seen
        
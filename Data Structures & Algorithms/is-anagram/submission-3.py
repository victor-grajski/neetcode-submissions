class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_seen = defaultdict(int)
        t_seen = defaultdict(int)

        # s: "jar"
        # t: "jam" 
        for c in s: # j, a, r
            s_seen[c] += 1
            # { j: 1 }
            # { j: 1, a: 1 }
            # { j: 1, a: 1, r: 1 }

        for c in t: # j, a, m
            t_seen[c] += 1
            # { j: 1 }
            # { j: 1, a: 1 }
            # { j: 1, a: 1, m: 1 }
        return s_seen == t_seen
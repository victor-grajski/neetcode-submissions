class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        res = []

        for s in strs:
            s_sorted = str(sorted(s))
            seen[s_sorted].append(s)
        for key in seen:
            res.append(seen[key])
        return res
        
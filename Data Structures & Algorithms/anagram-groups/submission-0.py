class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for i, word in enumerate(strs):
            word_sorted = str(sorted(word))

            if word_sorted not in seen:
                seen[word_sorted] = [word]
            else:
                seen[word_sorted].append(word)
        return list(seen.values())
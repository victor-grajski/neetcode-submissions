class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += "{0}#{1}".format(len(s), s)
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            separator_index = s.find('#', i)
            length = int(s[i:separator_index])
            decoded.append(s[separator_index + 1 : separator_index + length + 1])
            i = separator_index + length + 1
        return decoded
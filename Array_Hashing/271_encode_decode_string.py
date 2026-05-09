from typing import List


class Solution:
    # string length + # + string
    def encode(self, strs: List[str]) -> str:
        result = []
        for item in strs:
            result.append(str(len(item)) + '#' + item)
        return ''.join(result)

    # find # character, before # character, the integer value is the string length
    # after # character, go through up to string length index to get the string
    # starting index of the next string item is (index of # + 1 + string length of the previous item)
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1
            item_len = int(s[i:j])
            start = j + 1
            end = start + item_len
            result.append(s[start:end])

            i = end
        return result

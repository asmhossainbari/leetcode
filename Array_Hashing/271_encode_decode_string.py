from typing import List
class Solution:
    # string length + # + string
    def encode(self, strs: List[str]) -> str:
        result = ''
        for item in strs:
            result += str(len(item)) + '#' + item
        # print(f'encode result = {result}')
        return result

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
            result.append(s[j + 1: j + 1 + item_len])

            i = j + 1 + item_len
            # print(f'i = {i}')
        return result
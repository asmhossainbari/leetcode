import collections


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = collections.defaultdict(list)
        for str in strs:
            count = [0] * 26
            for s in str:
                count[ord(s) - ord('a')] += 1
            hashmap[tuple(count)].append(str)
        return hashmap.values()

strs = ["eat","tea","tan","ate","nat","bat"]
sol = Solution()
print(sol.groupAnagrams(strs))
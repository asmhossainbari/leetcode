class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq_hashmap = dict()
        for i in nums:
            if i in freq_hashmap:
                freq_hashmap[i] += 1
            else:
                freq_hashmap[i] = 1
        count = 0
        for key in freq_hashmap.copy():
            diff = k - key
            if diff in freq_hashmap:
                freq_val_1 = freq_hashmap[key]
                freq_val_2 = freq_hashmap[diff]
                if key != diff:
                    del freq_hashmap[key]
                    del freq_hashmap[diff]
                    count += min(freq_val_1, freq_val_2)
                else:
                    del freq_hashmap[key]
                    count += min(freq_val_1, freq_val_2) // 2

        return count


        
sol = Solution()
print(sol.maxOperations(nums=[2,5,4,4,1,3,4,4,1,4,4,1,2,1,2,2,3,2,4,2], k=3))
print(sol.maxOperations(nums=[1,2,3,4], k = 5))
print(sol.maxOperations(nums=[3,1,3,4,3], k =6))

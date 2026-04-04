from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        total_len = len(nums1) + len(nums2)
        half = (total_len + 1) // 2
        
        left = 0
        right = len(nums1)
        while left <= right:
            i = (left + right) // 2
            j = half - i
            leftA = nums1[i - 1] if i > 0 else float("-inf")
            rightA = nums1[i] if i < len(nums1) else float("inf")
            leftB = nums2[j - 1] if j > 0 else float("-inf")
            rightB = nums2[j] if j < len(nums2) else float("inf")
            if leftA <= rightB and leftB <= rightA:
                if total_len % 2 == 1:
                    return max(leftA, leftB)
                else:
                    return (max(leftA, leftB) + min(rightA, rightB) ) / 2.0
            if leftA > rightB:
                right = i - 1
            else:
                left = i + 1
        


sol = Solution()
print(sol.findMedianSortedArrays(nums1=[1, 3], nums2=[2]))  # 2.0
print(sol.findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]))  # 2.5
print(sol.findMedianSortedArrays(nums1=[0, 0], nums2=[0, 0]))  # 0.0
print(sol.findMedianSortedArrays(nums1=[], nums2=[1]))  # 1.0
print(sol.findMedianSortedArrays(nums1=[2], nums2=[]))  # 2.0
print(sol.findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4, 5]))  # 3.0
print(sol.findMedianSortedArrays(nums1=[1, 1], nums2=[1, 2]))  # 1.0
print(sol.findMedianSortedArrays(nums1=[-5, 3, 6], nums2=[-2, -1, 4]))  # 1.0

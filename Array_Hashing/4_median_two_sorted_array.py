class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i = 0
        j = 0
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        merged_arr = [0] * (len_nums1 + len_nums2)
        merged_arr_index = 0
        while i < len_nums1 and j < len_nums2:
            if nums1[i] <= nums2[j]:
                merged_arr[merged_arr_index] = nums1[i]
                i += 1
            else:
                merged_arr[merged_arr_index] = nums2[j]
                j += 1
            merged_arr_index += 1
        while i < len_nums1:
            merged_arr[merged_arr_index] = nums1[i]
            merged_arr_index += 1
            i += 1
        while j < len_nums2:
            merged_arr[merged_arr_index] = nums2[j]
            merged_arr_index += 1
            j += 1

        if (len_nums1 + len_nums2) % 2 == 0:
            m1 = int((len_nums1 + len_nums2 - 1) / 2.0)
            m2 = int((len_nums1 + len_nums2) / 2.0)
        else:
            m1 = int((len_nums1 + len_nums2) / 2.0)
            m2 = int((len_nums1 + len_nums2) / 2.0)
        return (merged_arr[m1] + merged_arr[m2]) / 2.0


nums1 = [1, 2]
nums2 = [3,7]
sol = Solution()
print(sol.findMedianSortedArrays(nums1=nums1, nums2=nums2))

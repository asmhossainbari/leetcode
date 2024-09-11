class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        hashmap = dict()
        for i in range(len(A)):
            for j in range(len(B)):
                zero_minus = 0 - (A[i] + B[j])
                if zero_minus not in hashmap:
                    hashmap[zero_minus] = 1
                else:
                    hashmap[zero_minus] += 1

        count = 0
        for i in range(len(C)):
            for j in range(len(D)):
                sum = C[i] + D[j]
                if sum in hashmap:
                    count += hashmap[sum]
        return count

A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]
sol = Solution()
print(sol.fourSumCount(A, B, C, D))


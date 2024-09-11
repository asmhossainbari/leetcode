class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = False
        reverse_num = 0
        if x < 0:
            negative = True
            x = -1 * x
        while x is not 0:
            div = x // 10
            mod = x % 10
            reverse_num = reverse_num * 10 + mod
            x = div
        if reverse_num > 2 ** 31:
            return 0
        if negative == True:
            return -1 * reverse_num
        else:
            return reverse_num


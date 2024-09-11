class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        input_number = x
        reverse_number = 0
        while x is not 0:
            div = x // 10
            mod = x % 10
            reverse_number = 10 * reverse_number + mod
            x = div

        if reverse_number == input_number:
            return True
        else:
            return False

a = Solution()
print(a.isPalindrome(132))
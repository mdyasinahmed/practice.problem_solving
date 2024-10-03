class Solution(object):
    def plusOne(self, digits):
        last = 1
        for i in reversed(xrange(len(digits))):
            digits[i] += last
            last = digits[i]/10
            digits[i] %= 10

        if last:
            digits = [1]+digits
        
        return digits
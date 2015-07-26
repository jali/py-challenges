class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        result = 0
        b = bin(n)
        bn = list(b)
        for i in bn:
            if i == '1':
                result += 1
        return result
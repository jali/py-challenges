class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return int(('%0*d' % (32, int(bin(n)[2:])))[::-1], 2)
#q2
def solution(A):
    N = len(A) + 1
    sum_N = (N * (N+1)) / 2
    return sum_N - sum(A)


    #binary = {0,b}.format(n)

def hammingWeight(n):
    result = 0
    b = bin(n)
    bn = list(b)
    for i in bn:
        if i == '1':
            result += 1
    return result

def solution(n):
	strbin = ('%0*d' % (32, int(bin(n)[2:])))[::-1]
	bbin = fbin[::-1]
	return int(bbin, 2)




def solution(n):
	ans = 0
    for i in range(32):
        ans <<= 1
        ans |= n & 1
        n >>= 1
    return ans




def solution(k, n):
	first = [i+1 for i in range(n)]
	result = []
	for x in range(n):
		result.append(first[x - k])
	return result


def solution(A):
	intersum = 0
	for i in range(len(A)):
		k = i + 1
		while (k < len(A)):
			if A[i] != A[k]:
				intersum += 1
			k += 1
		if intersum > 10000000:
			return -1
	return intersum


def solution(S):
	if 1 <= len(S) <= 100:
		arrwords = S.split()
		result =[]
		for element in arrwords:
			result.append(element[::-1])
		return " ".join(result)
	else:
		return -1


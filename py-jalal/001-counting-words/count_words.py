import sys
import re

def count_words(lines):
	result = {}
	for l in lines:
		line = re.findall(r'\w+', l)
		for word in line:
			w = word.lower()
			if len(w) > 1:
				if w in result:
					result[w] += 1
				else:
					result[w] = 1
	return sorted(result.iteritems(), key=lambda (k,v): (v,k), reverse=True)

if __name__ == '__main__':
    stream = sys.stdin
    lines = sys.stdin.readlines()
    for word, count in count_words(lines):
        print word, count

#!/usr/bin/python

def solution(x, y, d):
	cntmin = 0
	m = x
	while(m <= y):
		cntmin += 1
		m += d
		if (m >= y):
		    break
	
	return cntmin


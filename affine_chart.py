import numpy as np

nlist = \
[
	np.array([-1, -1, -1]),
	np.array([1, 0, 0]),
	np.array([0, 1, 0]),
	np.array([0, 0, 1]),
]

mlist = \
[
	np.array([1, 1, 1]),
	np.array([-3, 1, 1]),
	np.array([1, -3, 1]),
	np.array([1, 1, -3]),
]

def n(*args):
	return np.average([nlist[i] for i in args], axis=0)

def m(*args):
	return np.average([mlist[i] for i in args], axis=0)

def q(i, j, n):
	idx = [0,1,2,3]
	idx.remove(i)
	idx.remove(j)
	k, l = idx
	return [np.dot(m(k) - m(j), n)/4, np.dot(m(l) - m(j), n)/4]

def p(i, j, m):
	idx = [0,1,2,3]
	idx.remove(i)
	idx.remove(j)
	k, l = idx
	return [-np.dot(n(k) - n(j), m), -np.dot(n(l) - n(j), m)]

nl = [n(1), n(1, 3), n(1, 2), n(1, 2, 3)]
ml = [m(0), m(0, 2), m(0, 3), m(0, 2, 3)]
print(list(map(lambda n: q(1,0,n), nl)))
print(list(map(lambda n: p(0,1,n), ml)))

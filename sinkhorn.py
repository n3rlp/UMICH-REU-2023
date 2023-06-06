import matplotlib.pyplot as plt
import numpy as np
from random import random

eps = 0.1

def point_in_hull(point, hull):
	n = len(hull)
	for i in range(len(hull)):
		a, b, c = hull[i], hull[(i + 1) % n], hull[(i + 2) % n]
	if abs(point[0]) < 0.75 and abs(point[1]) < 0.75:
		return 1
	return 0
	### CHECK IF POINT IN HULL
	### RETURN 1 IF IN HULL, 0 ELSE

### Setup mesh for B
# range
bxrange = [-1, 1]
byrange = [-1, 1]

# number of gridpoints
bxnum = 40
bynum = 40

# mesh values
bx = np.linspace(*bxrange, bxnum)
by = np.linspace(*byrange, bynum)

# vertices of B, specified in anticlockwise order.
bpoints = \
[
	np.array([1, 0]),
	np.array([1, 1]),
	np.array([0, 1]),
	np.array([-1, 0]),
	np.array([-1, -1]),
	np.array([0, -1]),
]

# mu[p] corresponds to point p % bxnum, p // bxnum
mu = np.array([point_in_hull((x, y), bpoints) for y in by for x in bx])

#print([(x, y) for y in range(len(by)) for x in range(len(bx))])
mu = mu / np.sum(mu)

print(mu)

### Setup mesh for A
# range
axrange = [-1, 1]
ayrange = [-1, 1]

# number of gridpoints
axnum = 40
aynum = 40

# mesh values
ax = np.linspace(*axrange, axnum)
ay = np.linspace(*ayrange, aynum)

# vertices of B, specified in anticlockwise order.
apoints = \
[
	np.array([0, 0]),
	np.array([0, 1]),
	np.array([1, 0]),
]

nu = np.array([point_in_hull((x, y), apoints) for y in ay for x in ax])
nu = nu / np.sum(nu)

###########################################
###########################################

C = [[0 for _ in range(len(nu))] for _ in range(len(mu))]

for m in range(len(mu)):
	for n in range(len(nu)):
		mx = bx[m % bxnum]
		nx = ax[n % axnum]
		my = by[m // bxnum]
		ny = ay[n // axnum]
		C[m][n] = mx * nx + my * ny

C = np.exp(np.array(C) / eps)

l = np.ones(mu.shape)
p = np.ones(nu.shape)

steps = 10

for i in range(steps):
	if i % 100 == 0: print(i)

	l = mu/(C @ p)
	p = nu/(l @ C)

P = np.outer(l, p) * C

print(P)


l = l.reshape(bynum, bxnum)

f = list(P.argmax(axis = 1))
f = [(ax[i % axnum], ay[i // axnum]) for i in f]
f = np.array(f).reshape(bynum, bxnum, 2)
print(f)


fig = plt.figure(figsize = (12,10))
Ax = plt.axes(projection='3d')

X, Y = np.meshgrid(bx, by)
Z = -np.log(l) - 0.5*X*X - 0.5*Y*Y
#print(X, Y)

surf = Ax.plot_surface(X, Y, Z)

# Set axes label
Ax.set_xlabel('x', labelpad=20)
Ax.set_ylabel('y', labelpad=20)
Ax.set_zlabel('z', labelpad=20)

plt.show()

print(-np.log(l))
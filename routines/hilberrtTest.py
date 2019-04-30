from conGradient import conGradient
from steepestDesc import steepestDesc

hilbert4 = [[1 / (1 + i + j) for i in range(4)] for j in range(4)]
hilbert8 = [[1 / (1 + i + j) for i in range(8)] for j in range(8)]
hilbert16 = [[1 / (1 + i + j) for i in range(16)] for j in range(16)]
hilbert32 = [[1 / (1 + i + j) for i in range(32)] for j in range(32)]


print(conGradient(hilbert4, [[1] for i in range(4)], [[1] for i in range(4)], .000001, 10000))
print(conGradient(hilbert8, [[1] for i in range(8)], [[1] for i in range(8)], .000001, 10000))
print(conGradient(hilbert16, [[1] for i in range(16)], [[1] for i in range(16)], .000001, 10000))
print(conGradient(hilbert32, [[1] for i in range(32)], [[1] for i in range(32)], .000001, 10000))
print()
print()
print(steepestDesc(hilbert4, [[1] for i in range(4)], [[1] for i in range(4)], .00001, 1000000))
print(steepestDesc(hilbert8, [[1] for i in range(8)], [[1] for i in range(8)], .00001, 10000))
print(steepestDesc(hilbert16, [[1] for i in range(16)], [[1] for i in range(16)], .00001, 10000))
print(steepestDesc(hilbert32, [[1] for i in range(32)], [[1] for i in range(32)], .00001, 10000))
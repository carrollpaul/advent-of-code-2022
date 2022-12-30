import numpy as np
from rich import print

count = 0
with open("input.txt") as f:
    forest = np.array([list(map(int, line.rstrip())) for line in f.readlines()])

    for i in range(forest.shape[0]):
        for j in range(forest.shape[1]):
            pass


R = lambda v: range(len(v))
E = enumerate
F = lambda m: [r[::-1] for r in m]  # flip horizontally
T = lambda m: [[m[j][i] for j in R(m[0])] for i in R(m)]  # transpose
G = lambda v: [int(i == 0 or e > v[i - 1]) for i, e in E(v)]  # step/grad
M = lambda v: [m := max(m, e) if i else (m := e) for i, e in E(v)]  # max
X = lambda m: [G(M(v)) for v in m]  # one-direction solution
O = lambda m, n: [[a | n[i][j] for j, a in E(e)] for i, e in E(m)]  # or
S = lambda m: sum(sum(v) for v in m)  # sum
L = lambda e, v: [int(e <= x) for i, x in E(v)].index(1) + 1  # location
Y = lambda e, v: len(v) if all(e > x for x in v) else L(e, v)  # one dir
Z = lambda e, i, v: Y(e, v[i + 1 :]) * Y(e, v[:i][::-1])  # two dirs

t = [[int(c) for c in l.strip()] for l in open("input.txt", "rt")]
u = T(t)
p = S(O(O(X(t), F(X(F(t)))), O(T(X(T(t))), T(F(X(F(T(t))))))))
q = max(max(Z(v, i, w) * Z(v, j, u[i]) for i, v in E(w)) for j, w in E(t))
print(p, q)

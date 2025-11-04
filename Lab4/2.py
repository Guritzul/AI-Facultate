x1 = 1
x2 = 2
y = 5
c = 0.01

w1n1 = 0.1
w2n1 = 0.2

o = w1n1 * x1 + w2n1 * x2

E = 0.5 * (y - o) ** 2

while E > 0.0001:
    w1n2 = w1n1 - c * (y - o) * (-x1)
    w2n2 = w2n1 - c * (y - o) * (-x2)
    w1n1, w2n1 = w1n2, w2n2
    print(w1n1, w2n1)
    o = w1n1 * x1 + w2n1 * x2
    E = 0.5 * (y - o) ** 2
    print(E)

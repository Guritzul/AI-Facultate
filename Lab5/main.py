import math


#Ex1

x1 = [1, -2, 1.5, 0]
x2 = [1, -0.5, -2, -1.5]
x3 = [0, 1, -1, 1.5]

intrari = [x1, x2, x3]

w = [1, -1, 0, 0.5]
wNew = [0, 0, 0, 0]


#Ex2

# x1 = [1, -2]
# x2 = [0, 1]
# x3 = [2, 3]
# x4 = [1, -1]

# intrari = [x1, x2, x3, x4]

# w = [1, -1]
# wNew = [0, 0]


for x in intrari:

    net = 0
    for i in range(len(w)):
        net += w[i] * x[i]
    print(net)
    if net >=0:
        for i in range(len(w)):
            wNew[i] = w[i] + x[i]
    else:
        for i in range(len(w)):
            wNew[i] = w[i] - x[i]
    w = wNew.copy()
    net = 0
    print(w)

print("---- TANH ----")

#Ex1

w = [1, -1, 0, 0.5]
wNew = [0, 0, 0, 0]

#Ex2

# w = [1, -1]
# wNew = [0, 0]


for x in intrari:
    net = 0
    for i in range(len(w)):
        net += w[i] * x[i]
    f = math.tanh(net/2)
    for i in range(len(w)):
        wNew[i] = w[i] + f * x[i]
    w = wNew.copy()
    net = 0
    print([round(num ,3) for num in w])
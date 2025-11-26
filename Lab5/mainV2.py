import math

def update_w(w, x, use_tanh=False):
    net = sum(w[i] * x[i] for i in range(len(w)))
    if use_tanh:
        f = math.tanh(net / 2)
    else:
        f = 1 if net >= 0 else -1
    return [w[i] + f * x[i] for i in range(len(w))]


intrari = [
    [1, -2, 1.5, 0],
    [1, -0.5, -2, -1.5],
    [0, 1, -1, 1.5]
]

w = [1, -1, 0, 0.5]


# intrari = [
#   [1, -2],
#   [0, 1],
#   [2, 3],
#   [1, -1]
# ]
# w = [1, -1]

for x in intrari:
    net = sum(w[i] * x[i] for i in range(len(w)))
    print(net)
    w = update_w(w, x, use_tanh=False)
    print(w)

print("activare continua")
w = [1, -1, 0, 0.5] 
#w = [1, -1]
for x in intrari:
    w = update_w(w, x, use_tanh=True)
    print([round(num, 3) for num in w])
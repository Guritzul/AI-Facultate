import random

points = [[45,85], (50,43), (40,80), (55,42), (200,43), (48,40), (195,41), (43,87), (190,40)]

c = 0.1 # coeficient de invatare

p = 3 # nr prototipuri

nrEpoch = 100

w = [[random.randint(0,200), random.randint(0,200)],[random.randint(0,200), random.randint(0,200)],
     [random.randint(0,200), random.randint(0,200)]] # prototipuri

print("w initial:")
print(w)


def distance(a, b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5

for epoch in range(nrEpoch):
    for point in points:
        distante = []
        for prototype in w:
            d = distance(point, prototype)
            distante.append(d)
        winnerPrototype = distante.index(min(distante))
        oldPrototype = w[winnerPrototype]
        newPrototype = [oldPrototype[0] + c * (point[0] - oldPrototype[0]),
                        oldPrototype[1] + c * (point[1] - oldPrototype[1])]
        w[winnerPrototype] = newPrototype
print("\w final:")
print(w)

grupuri = {0: [], 1: [], 2: []}

for point in points:
    distante = []
    for prototype in w:
        d = distance(point, prototype)
        distante.append(d)
    winnerPrototype = distante.index(min(distante))
    grupuri[winnerPrototype].append(point)

for i in range(p):
    print(f"\nPrototipl {i+1} a ajuns la: {w[i]}")
    print(f"Punctele din grupul {i+1} sunt: {grupuri[i]}")
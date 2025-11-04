start_value = 10

x1 = start_value
x2 = 0
c = 0.1

while True:
    x2 = x1 - c*(6*x1 - 6)
    print (x2)
    if x1 - x2 < 0.0001:
        break
    else:
        x1 = x2

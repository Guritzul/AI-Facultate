weights = [0.1, -0.8, -1.1, 0.6]

with open('iris.data', 'r') as f:
    line = f.readline().strip()
    valLine1 = [float(val) for val in line.split(',')[:4] if val]
    weighted_sum1 = sum(val * weight for val, weight in zip(valLine1, weights))
    print("Suma ponderată a valorilor din prima linie este:", weighted_sum1)
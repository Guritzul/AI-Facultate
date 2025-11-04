with open("iris.data", "r") as f:
    valCol1 = [float(line.split(",")[0]) for line in f if line.strip()]
    valMediana1 = sorted(valCol1)
    n1 = len(valMediana1)
    if n1 % 2 == 1:
        mediana1 = valMediana1[n1 // 2]
    else:
        mediana1 = (valMediana1[n1 // 2 - 1] + valMediana1[n1 // 2]) / 2
    print("Valoarea mediana din prima coloană este:", mediana1)

with open("iris.data", "r") as f:
    valCol2 = [float(line.split(",")[1]) for line in f if line.strip()]
    valMediana2 = sorted(valCol2)
    n2 = len(valMediana2)
    if n2 % 2 == 1:
        mediana2 = valMediana2[n2 // 2]
    else:
        mediana2 = (valMediana2[n2 // 2 - 1] + valMediana2[n2 // 2]) / 2
    print("Valoarea mediana din a doua coloană este:", mediana2)

with open("iris.data", "r") as f:
    valCol3 = [float(line.split(",")[2]) for line in f if line.strip()]
    valMediana3 = sorted(valCol3)
    n3 = len(valMediana3)
    if n3 % 2 == 1:
        mediana3 = valMediana3[n3 // 2]
    else:
        mediana3 = (valMediana3[n3 // 2 - 1] + valMediana3[n3 // 2]) / 2
    print("Valoarea mediana din a treia coloană este:", mediana3)

with open("iris.data", "r") as f:
    valCol4 = [float(line.split(",")[3]) for line in f if line.strip()]
    valMediana4 = sorted(valCol4)
    n4 = len(valMediana4)
    if n4 % 2 == 1:
        mediana4 = valMediana4[n4 // 2]
    else:
        mediana4 = (valMediana4[n4 // 2 - 1] + valMediana4[n4 // 2]) / 2
    print("Valoarea mediana din a patra coloană este:", mediana4)

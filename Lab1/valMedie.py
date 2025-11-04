with open("iris.data", "r") as f:
    valCol1 = [float(line.split(",")[0]) for line in f if line.strip()]
valMedie1 = sum(valCol1) / len(valCol1)
print("Valoarea medie din prima coloană este:", valMedie1)

with open("iris.data", "r") as f:
    valCol2 = [float(line.split(",")[1]) for line in f if line.strip()]
valMedie2 = sum(valCol2) / len(valCol2)
print("Valoarea medie din a doua coloană este:", valMedie2)

with open("iris.data", "r") as f:
    valCol3 = [float(line.split(",")[2]) for line in f if line.strip()]
valMedie3 = sum(valCol3) / len(valCol3)
print("Valoarea medie din a treia coloană este:", valMedie3)

with open("iris.data", "r") as f:
    valCol4 = [float(line.split(",")[3]) for line in f if line.strip()]
valMedie4 = sum(valCol4) / len(valCol4)
print("Valoarea medie din a patra coloană este:", valMedie4)
with open("c:\\Users\\andre\\Documents\\AI\\Lab1\\iris.data", "r") as f:
    valCol1 = [float(line.split(",")[0]) for line in f if line.strip()]
valMin1 = min(valCol1)
print("Cea mai mică valoare din prima coloană este:", valMin1)

with open("c:\\Users\\andre\\Documents\\AI\\Lab1\\iris.data", "r") as f:
    valCol2 = [float(line.split(",")[1]) for line in f if line.strip()]
valMin2 = min(valCol2)
print("Cea mai mică valoare din a doua coloană este:", valMin2)

with open("c:\\Users\\andre\\Documents\\AI\\Lab1\\iris.data", "r") as f:
    valCol3 = [float(line.split(",")[2]) for line in f if line.strip()]
valMin3 = min(valCol3)
print("Cea mai mică valoare din a treia coloană este:", valMin3)

with open("c:\\Users\\andre\\Documents\\AI\\Lab1\\iris.data", "r") as f:
    valCol4 = [float(line.split(",")[3]) for line in f if line.strip()]
valMin4 = min(valCol4)
print("Cea mai mică valoare din a patra coloană este:", valMin4)
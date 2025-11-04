with open("c:\\Users\\andre\\Documents\\AI\\Lab1\\iris.data", "r") as f:
    valCol1 = [float(line.split(",")[0]) for line in f if line.strip()]
valMax1 = max(valCol1)

with open("c:\\Users\\andre\\Documents\\AI\\Lab1\\iris.data", "r") as f:
    valCol2 = [float(line.split(",")[1]) for line in f if line.strip()]
valMax2 = max(valCol2)

with open("c:\\Users\\andre\\Documents\\AI\\Lab1\\iris.data", "r") as f:
    valCol3 = [float(line.split(",")[2]) for line in f if line.strip()]
valMax3 = max(valCol3)

with open("c:\\Users\\andre\\Documents\\AI\\Lab1\\iris.data", "r") as f:
    valCol4 = [float(line.split(",")[3]) for line in f if line.strip()]
valMax4 = max(valCol4)

print("Cea mai mare valoare din prima coloană este:", valMax1)
print("Cea mai mare valoare din a doua coloană este:", valMax2)
print("Cea mai mare valoare din a treia coloană este:", valMax3)
print("Cea mai mare valoare din a patra coloană este:", valMax4)
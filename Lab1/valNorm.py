import valMax
import valMin

xNorm = [150]

with open("c:\\Users\\andre\\Documents\\AI\\Lab1\\iris.data", "r") as f:
    valCol1 = [float(line.split(",")[0]) for line in f if line.strip()]
    for i in range(len(valCol1)):
        valCol1[i] = (valCol1[i] - valMin.valMin1) / (valMax.valMax1 - valMin.valMin1)
        print(f"Valoarea normalizată din coloana 1 este:", valCol1[i])

with open("c:\\Users\\andre\\Documents\\AI\\Lab1\\iris.data", "r") as f:
    valCol2 = [float(line.split(",")[1]) for line in f if line.strip()]
    for j in range(len(valCol2)):
        valCol2[j] = (valCol2[j] - valMin.valMin2) / (valMax.valMax2 - valMin.valMin2)
        print(f"Valoarea normalizată din coloana 2 este:", valCol2[j])

with open("c:\\Users\\andre\\Documents\\AI\\Lab1\\iris.data", "r") as f:
    valCol3 = [float(line.split(",")[2]) for line in f if line.strip()]
    for k in range(len(valCol3)):
        valCol3[k] = (valCol3[k] - valMin.valMin3) / (valMax.valMax3 - valMin.valMin3)
        print(f"Valoarea normalizată din coloana 3 este:", valCol3[k])

with open("c:\\Users\\andre\\Documents\\AI\\Lab1\\iris.data", "r") as f:
    valCol4 = [float(line.split(",")[3]) for line in f if line.strip()]
    for m in range(len(valCol4)):
        valCol4[m] = (valCol4[m] - valMin.valMin4) / (valMax.valMax4 - valMin.valMin4)
        print(f"Valoarea normalizată din coloana 4 este:", valCol4[m])
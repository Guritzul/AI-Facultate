with open('iris.data', 'r') as file:
    data = file.readlines()

date_setosa = []
date_versicolor = []

for line in data:
    parts = line.strip().split(',')
    if len(parts) == 5:
        valori = list(map(float, parts[:4]))
        specie = parts[4]
        # print(f"{valori},{specie}")

        if specie == 'Iris-setosa':
            date_setosa.append([valori, 1])
        elif specie == 'Iris-versicolor':
            date_versicolor.append([valori, -1])

# print(len(date_setosa), len(date_versicolor))
        

date_antrenare = date_setosa[:5] + date_versicolor[:5]
date_testare = date_setosa[5:] + date_versicolor[5:]
# print(date_antrenare)
# print(len(date_testare))

w = [0.1, 0.2, 0.3, 0.4]
c = 0.1

for epica in range(100):
    eroare = 0

    for date in date_antrenare:
        intrari = date[0]
        rapsunsuri = date[1]

        net = 0

        for i in range(len(w)):
            net += w[i] * intrari[i]
        
        if net >= 0:
            for i in range(len(w)):
                w[i] += c * (rapsunsuri - 1) * intrari[i]
            
            if rapsunsuri != 1:
                eroare += 1

        else:
            for i in range(len(w)):
                w[i] += c * (rapsunsuri + 1) * intrari[i]

            if rapsunsuri != -1:
                eroare += 1
                
    # print(f"epoca {epica+1}, eroare: {eroare}")
    if eroare == 0:
        break

print("w final:", w)

raspunsuriCorecte = 0

for date in date_testare:
    intrari = date[0]
    rapsunsuri = date[1]

    net = 0

    for i in range(len(w)):
        net += w[i] * intrari[i]
    
    if net >=0:
        numar = 1
    else:
        numar = -1
    
    if numar == rapsunsuri:
        raspunsuriCorecte += 1

print("raspunsuri corecte:", raspunsuriCorecte, "/", len(date_testare))
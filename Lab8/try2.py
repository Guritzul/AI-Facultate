import random
import math

coordonate = [(45, 85), (50, 43), (40, 80), (55, 42), (200, 43), (48, 40), (195, 41), (43, 87), (190, 40)]

NR_GRUPURI = 3

def distanta(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def centru_apropiat(punct, lista_centroizi):
    distante = [distanta(punct, c) for c in lista_centroizi]
    return distante.index(min(distante))

def algoritm(date, k):
    pivoti = random.sample(date, k)
    #pivoti = [(45, 85), (200, 43), (48, 40)]  # Test
    print(f"Pivoti initiali: {pivoti}\n")
    
    for iteratie in range(10): 
        grupuri = [[] for _ in range(k)]
    
        for p in date:
            index_ales = centru_apropiat(p, pivoti)
            grupuri[index_ales].append(p)
        
        pivoti_noi = []
        for i, grup in enumerate(grupuri):
            if grup:
                media_x = sum(p[0] for p in grup) / len(grup)
                media_y = sum(p[1] for p in grup) / len(grup)
                pivoti_noi.append((media_x, media_y))
            else:
                pivoti_noi.append(pivoti[i])
        
        if pivoti == pivoti_noi:
            print(f"S-a oprit la iteratia {iteratie} (convergenta atinsa).")
            break
            
        pivoti = pivoti_noi

    return pivoti, grupuri

centroizi_finali, clustere_finale = algoritm(coordonate, NR_GRUPURI)

for i in range(NR_GRUPURI):
    print(f"\nGRUPUL {i + 1}:")
    print(f"   Centroid: {centroizi_finali[i]}")
    print(f"   Puncte:   {clustere_finale[i]}")
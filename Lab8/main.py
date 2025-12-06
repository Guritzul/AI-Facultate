import random
import math

points = [
    (45, 85), (50, 43), (40, 80), 
    (55, 42), (200, 43), (48, 40), 
    (195, 41), (43, 87), (190, 40)
]

K = 3

centroids = random.sample(points, K)
print(f"AStia initiali - {centroids}")

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

for iteration in range(100):
    clusters = [[] for _ in range(K)]

    for point in points:
        distances = [distance(point, centroid) for centroid in centroids]
        closest_centroid = distances.index(min(distances))
        clusters[closest_centroid].append(point)
    
    newCentroids = []
    for cluster in clusters:
        if cluster:
            x = sum(p[0] for p in cluster) / len(cluster)
            y = sum(p[1] for p in cluster) / len(cluster)
            newCentroids.append((x, y))
        else:
            #print("Nush inca") aici las clusterul ca la incept
            newCentroids.append(centroids[i])
    centroids = newCentroids
#print(centroids)

print("\nREzultate")
for i in range(K):
    print({i+1})
    print(f"Centoridul{centroids[i]}")
    print(f"Punctele din clueter{clusters[i]}")

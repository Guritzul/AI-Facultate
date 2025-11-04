points = [(-1,-1,-1), (-1,-1,1), (-1,1,-1), (-1,1,1), (1,-1,-1), (1,-1,1), (1,1,-1), (1,1,1)]

for i in range(len(points)):
    points[i] = sum(points[i])
    if points[i] < 0:
        points[i] = -1
    else:
        points[i] = 1
print(points)    

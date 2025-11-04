numbers = [(1,1,1,1,0,1,1,1,1),
           (0,1,0,1,0,1,0,1,0),
           (0,1,0,0,1,0,0,1,0),
           (1,1,0,0,1,0,0,1,0)]

for i in range(len(numbers)):
    numbers[i] = numbers[i][0]*-0.14 + numbers[i][1]*0.06 + numbers[i][2]*-0.28 + numbers[i][3]*-0.93 + numbers[i][4]*-0.08 + numbers[i][5]*0.28 + numbers[i][6]*-0.64 + numbers[i][7]*0.47 + numbers[i][8]*-0.85
    if numbers[i] > 0:
        numbers[i] = 1
    else:
        numbers[i] = 0
print(numbers)
import random

minValue = -512
maxValue = 512

bitsPerValue = 10

totalLength = bitsPerValue * 3  #pentru ca x, y, z
populationSize = 20  #aici bag o valoare radmom pentru tst
generations = 100   #10 de test

error = 0.0001 #o sa ma nevoie mai incolo pot lua orice valoare mai mica decat 1

crossoverRate = 0.7
muttationRate = 0.01

def generatePopulation(populationSize, totalLength):
    population = []
    for _ in range(populationSize):
        individual = ''.join(random.choice('01') for _ in range(totalLength))
        population.append(individual)
    return population

#deasupra generez populatia de 0 si 1

# population = generatePopulation(populationSize, totalLength)
# for individual in population:
#     print(individual) #verufucare 

def decodeIndividual(individual):
    bitiX = individual[0:10] 
    bitiY = individual[10:20]
    bitiZ = individual[20:30]

    valoareX = int(bitiX, 2)
    valoareY = int(bitiY, 2)
    valoareZ = int(bitiZ, 2)

    x = minValue + (valoareX / (2**bitsPerValue - 1)) * (maxValue - minValue)
    y = minValue + (valoareY / (2**bitsPerValue - 1)) * (maxValue - minValue)
    z = minValue + (valoareZ / (2**bitsPerValue - 1)) * (maxValue - minValue)

    return x, y, z

# for individual in generatePopulation(populationSize, totalLength):
#     x, y, z = decodeIndividual(individual)
#     print(f"Individual: {individual} => x: {x}, y: {y}, z: {z}")    

#s-ar putea sa mai fie nevoie de chestia asat ed sus mai adaugi chestii dupa

#aici imi deja imi regret deciziile in viata uhhh test sa vad ce-mi da*

def calulateFitness(x, y, z):
    fitness = x**2 + y**2 + z**2
    return 1/(fitness + error)

# for individual in generatePopulation(populationSize, totalLength):
#     x, y, z = decodeIndividual(individual)
#     fitness = calulateFitness(x, y, z)
#     print(f"Individual: {individual} => x: {x}, y: {y}, z: {z}, Fitness: {fitness}")

#asta de sus e alt test

def selectareParinti(population, fitnessValues):
    parents = random.choices(population, weights=fitnessValues, k=len(population))
    return parents

population = generatePopulation(populationSize, totalLength)
fitnessValues = []

for individual in population:
    x, y, z = decodeIndividual(individual)
    fitness = calulateFitness(x, y, z)
    fitnessValues.append(fitness)

parents = selectareParinti(population, fitnessValues)

# for i, individual in enumerate(parents):
#     x, y, z = decodeIndividual(individual)
#     fitness = calulateFitness(x, y, z)
#     print(f"Parent {i+1}: {individual} => x: {x}, y: {y}, z: {z}, Fitness: {fitness}")

def crossover(parent1, parent2):
    if random.random() < crossoverRate:
        point = random.randint(1,  len(parent1) - 1)
        
        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]

        return child1, child2
    
    else:
        return parent1, parent2
    
nextGeneration = []
for i in range(0, len(parents), 2):
    parent1 = parents[i]
    parent2 = parents[i+1]
    
    child1, child2 = crossover(parent1, parent2)
    
    nextGeneration.append(child1)
    nextGeneration.append(child2)

# for i, individual in enumerate(nextGeneration):
#     x, y, z = decodeIndividual(individual)
#     fitness = calulateFitness(x, y, z)
#     print(f"Child {i+1}: {individual} => x: {x}, y: {y}, z: {z}, Fitness: {fitness}")

def mutate(individual):
    individualList = list(individual)

    for i in range(len(individualList)):
        if random.random() < muttationRate:
            individualList[i] = '1' if individualList[i] == '0' else '0'

    return ''.join(individualList)

mutatedGeneration = []
for individual in nextGeneration:
    mutatedIndividual = mutate(individual)
    mutatedGeneration.append(mutatedIndividual)

# for i, individual in enumerate(mutatedGeneration):
#     x, y, z = decodeIndividual(individual)
#     fitness = calulateFitness(x, y, z)
#     print(f"Mutated Child {i+1}: {individual} => x: {x}, y: {y}, z: {z}, Fitness: {fitness}")

population =  generatePopulation(populationSize, totalLength)

for generation in range(generations):
    fitnessValues = []
    decodedValues = []

    for individual in population:
        x, y, z = decodeIndividual(individual)
        fitness = calulateFitness(x, y, z)
        fitnessValues.append(fitness)
        decodedValues.append((x, y, z))
    
    bestFitness = max(fitnessValues)
    bestIndex = fitnessValues.index(bestFitness)
    print(f"Generation {generation + 1}: Best Fitness: {bestFitness:.4f}, x: {decodedValues[bestIndex][0]:.4f}, y: {decodedValues[bestIndex][1]:.4f}, z: {decodedValues[bestIndex][2]:.4f}")

    parents = selectareParinti(population, fitnessValues)

    nextGeneration = []
    for i in range(0, len(parents), 2):
        parent1 = parents[i]
        parent2 = parents[i+1]
        
        child1, child2 = crossover(parent1, parent2)
        
        child1 = mutate(child1)
        child2 = mutate(child2)

        nextGeneration.append(child1)
        nextGeneration.append(child2)
    
    population = nextGeneration


#s-ar putea sa fie linii in plsu dar imi e prea lene sa le sterg las asta pe alta data
#pot muta def-urile la inceput sau in alte fisiere dar las asta pe alta data
#daca vezi asta nu stii ce face codul asa ca mai bine nu te chinui sa-l intelegi
#daca te intorci vreodata la acest cod sterge toate "testele"
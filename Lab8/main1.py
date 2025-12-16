import random

length = 6
populationSize = 10
generations = 5
mutationRate = 0.1

def generatePopulation(populationSize, length):
    population = []
    for _ in range(populationSize):
        individual = ''.join(random.choice('01') for _ in range(length))
        population.append(individual)
    return population

def decodeIndividual(individual):
    return int(individual, 2)

def calculateFitness(individual):
    return 1.0/(individual + 1)

def selectareParinti(population, fitnessValues):
    return random.choices(population, weights=fitnessValues, k=len(population))

def crossover(parent1, parent2):
    point = random.randint(1, length - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

def mutate(individual):
    individual = list(individual)
    for i in range(len(individual)):
        if random.random() < mutationRate:
            individual[i] = '1' if individual[i] == '0' else '0'
    return ''.join(individual)

population = generatePopulation(populationSize, length)

for generation in range(generations):
    fitnessValues = []
    decodedValues = []

    for individual in population:
        decoded = decodeIndividual(individual)
        decodedValues.append(decoded)
        fitness = calculateFitness(decoded)
        fitnessValues.append(fitness)

    bestValue = min(decodedValues)
    print(f"Generation {generation}: Best Value = {bestValue}")

    parents = selectareParinti(population, fitnessValues)

    nextGeneration = []
    for i in range(0, len(parents), 2):
        parent1 = parents[i]
        parent2 = parents[i + 1]
        child1, child2 = crossover(parent1, parent2)
        nextGeneration.append(mutate(child1))
        nextGeneration.append(mutate(child2))

    population = nextGeneration[:populationSize]
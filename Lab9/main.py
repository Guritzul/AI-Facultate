import random

cards = 10
populationSize = 50
crossoverRate = 0.7
mutationRate = 0.01
generations = 100

targetSum = 36
targetProduct = 360

def generateDeck(populationSize):
    deck = []
    for _ in range(populationSize):
        card = ''.join(random.choice('01') for _ in range(cards))
        deck.append(card)
    return deck

print(generateDeck(populationSize))

def calculateFitness(card):
    deckSum = 0
    deckProduct = 1

    for i in range(len(card)):
        if card[i] == '0':
            deckSum += i+1
        else:
            deckProduct *= i+1

    
    errorSum = abs(targetSum - deckSum)
    errorProduct = abs(targetProduct - deckProduct)

    totalError = errorSum + errorProduct
    
    return 1.0 / (1 + totalError)

def stats(deck):
    sum = 0
    product = 1
    sumDeck = []
    productDeck = []
    for i in range(len(deck)):
        if deck[i] == '0':
            sum += i+1
            sumDeck.append(i+1)
        else:
            product *= i+1
            productDeck.append(i+1)
    return sum, product, sumDeck, productDeck

def selectParents(population, fitnessValues):
    return random.choices(population, weights=fitnessValues, k=len(population))

def crossover(parent1, parent2):
    if random.random() < crossoverRate:
        point = random.randint(1, len(parent1) - 1)
        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]
        return child1, child2
    else:
        return parent1, parent2
    
def mutate(card, mutationRate):
    cardList = list(card)
    for i in range(len(cardList)):
        if random.random() < mutationRate:
            cardList[i] = '1' if cardList[i] == '0' else '0'
    return ''.join(cardList)

population = generateDeck(populationSize)

for generation in range(generations):

    fitnessValues = []
    solutionFound = False

    for card in population:
        fitness = calculateFitness(card)
        fitnessValues.append(fitness)

        if fitness == 1.0:
            sum, product, sumDeck, productDeck = stats(card)
            print(f"Solution found in generation {generation}: {card} => Sum: {sum} ({sumDeck}), Product: {product} ({productDeck})")
            solutionFound = True
            break
    
    if solutionFound:
        break

    parents = selectParents(population, fitnessValues)

    nextGeneration = []
    for i in range(0, len(parents), 2):
        parent1 = parents[i]
        parent2 = parents[i+1]
        child1, child2 = crossover(parent1, parent2)
        child1 = mutate(child1, mutationRate)
        child2 = mutate(child2, mutationRate)
        nextGeneration.append(child1)
        nextGeneration.append(child2)

    population = nextGeneration


    bestFitness = max(fitnessValues)
    print(f"Generation {generation}: Best Fitness = {bestFitness}")
    bestIndividual = population[fitnessValues.index(bestFitness)]
    sum, product, sumDeck, productDeck = stats(bestIndividual)
    print(f"  Best Individual: {bestIndividual} => Sum: {sum} ({sumDeck}), Product: {product} ({productDeck})")
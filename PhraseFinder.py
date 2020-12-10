import random

# target word and entire alphabet to generate random starting population
target_word = "hi"
alphabet = "abcdefghijklmnopqrstuvwxyz "

word_size = len(target_word)

# population size; optimal is 26 and above to have
# plenty individuals with high fitness
POP_SIZE = 600

# holds a population
population = []
# holds the fitness of each individual of the population
allFitness = []

def generateIndividual(lettersUsed, size):
    """ generates a single word """
    # holds final word
    random_word = ""

    for i in range(size):
        # generate random letter
        index = random.randint(0, len(lettersUsed)-1)
        random_word += lettersUsed[index]
    return random_word

def calculateFitness(word, targetWrd):
    """ calculates the fitness of the parameter word.
    Fitness is calculated by checking how many letters
    match the position and character of the target word """
    # the fitness to return
    fitness = 1
    for i in range(len(word)):
        # increment fitness when characters at position i match
        if word[i] == targetWrd[i]:
            fitness += 1

    return fitness

def mate(words, population_s):
    """ mates (single-point crossover)
    population*2 words to form a POP_SIZE new
    population with better overall fitness """
    new_population = []
    for i in range(population_s//2):
        # select two words at random
        word1 = random.choice(words)
        word2 = random.choice(words)

        # mate word1 and word2 then append 2 children to new population
        crossover_point = random.randint(0, len(word1))
        offspring1 = word1[0:crossover_point] + word2[crossover_point:]
        offspring2 = word2[0:crossover_point] + word1[crossover_point:]

        # for mutation
        mutation_probability = random.uniform(0, 1)
        if mutation_probability <= 0.05:
            yes_no = [1, 0]
            if (random.choice(yes_no) == 1):
                offspring1.replace(offspring1[random.randint(0, len(offspring1)-1)], alphabet[random.randint(0, len(alphabet)-1)])
            else:
                offspring2.replace(offspring2[random.randint(0, len(offspring2)-1)], alphabet[random.randint(0, len(alphabet)-1)])

        # now append to new population
        new_population.append(offspring1)
        new_population.append(offspring2)

    return new_population

def targetFound(population, target):
    """ checks if the target phrase has been found yet """
    for word in population:
        if word == target:
            return True

# generate individuals as members of the population
for i in range(POP_SIZE):
    population.append(generateIndividual(alphabet, word_size))

# calculate fitness for each word and make new population
# that holds words of higher fitness more frequently
new_population = []
for each_word in population:
    new_population += [each_word] * calculateFitness(each_word, target_word)


newby = mate(new_population, POP_SIZE)
for word in newby:
    print(word)

# keep the best parent of the last generation
best = max(newby)

# to keep track of the number of generations necessary to find the phrase.
# 1 generation is already complete due to the above code
gener = 1
while (not targetFound(newby, target_word)):
    new_population = []
    new_population.append(best)

    # for each word in the population calculate it's fitness
    # and place it into a new array fitness times so that it has
    # a higher chance of getting chosen
    for each_word in newby:
        print(each_word)
        new_population += [each_word] * calculateFitness(each_word, target_word)

    #print("more frequent", new_population)
    newby = mate(new_population, POP_SIZE)

    # reset the best of the last population
    best = max(newby)
    #print("new", newby)
    #print()

    # increment the number of generations that have been taken
    gener += 1

# print the index of the found target
newby[len(newby)-1] = newby[newby.index(target_word)]
print(newby[len(newby)-1])
print()
print("Total number of generations is:", gener)





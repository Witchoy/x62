from numpy import random

def random_population(nb_tours, n):
    pop = []
    for i in range(nb_tours):
        temp = random.permutation(n)
        pop.append(temp)
    
    return pop

def displacement_mutation(tour):
    i1 = random.randint(len(tour))
    i2 = random.randint(len(tour))
    if i1 > i2:
        i1, i2 = i2, i1

    seg = tour[i1:i2+1]
    rest = list(tour[:i1]) + list(tour[i2+1:])
    insert_pos = random.randint(len(rest) + 1)
    return rest[:insert_pos] + list(seg) + rest[insert_pos:]

def exchange_mutation(tour):
    i1 = random.randint(len(tour))
    i2 = random.randint(len(tour))

    ele1, ele2 = tour[i1], tour[i2]
    tour[i1], tour[i2] = ele2, ele1
    return tour

def cycle_crossover(parent1, parent2):
    temp = [0] * len(parent1)
    for i in range(len(parent1)):
        temp[i] = 

def main():
    populations = random_population(3, 10)

    # for i in range(3):
    #     print(populations[i])

    return 0

main()
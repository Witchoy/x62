"""
TP1 - Algorithmes génétiques
Travelling Salesman Problem (TSP) - Genetic Algorithm
"""

import random
from tsp_utils import tour_length

def random_population(nb_tours, n):
    tours = []
    
    for i in range(nb_tours):
        tours.append(random.sample(range(1, n+1), n))

    return tours


def displacement_mutation(tour):
    i1, i2 = random.randint(0, len(tour)-1), random.randint(0, len(tour)-1)
    if i2 < i1:
        i1, i2 = i2, i1
    subsequence = tour[i1:i2+1]
    temp = tour[:i1] + tour[i2+1:]
    insert_pos = random.randint(0, len(temp) + 1)
    return temp[:insert_pos] + subsequence + temp[insert_pos:]


def exchange_mutation(tour):
    tour_cpy = tour.copy()
    i1, i2 = random.randint(0, len(tour)-1), random.randint(0, len(tour)-1)
    tour_cpy[i1], tour_cpy[i2] = tour[i2], tour[i1]
    return tour_cpy


def cycle_crossover(parent1, parent2):
    n = len(parent1)

    visited = [False] * n
    cycles = []

    for i in range(n):
        if visited[i]:
            continue

        cycle = []
        current = i

        while True:
            cycle.append(current)
            visited[current] = True
            current = parent2.index(parent1[current])
            if current == i:
                break

        cycles.append(cycle)

    child1 = [None] * n
    child2 = [None] * n

    for c, cycle in enumerate(cycles):
        for idx in cycle:
            if c % 2 == 0:
                child1[idx] = parent1[idx]
                child2[idx] = parent2[idx]
            else:
                child1[idx] = parent2[idx]
                child2[idx] = parent1[idx]

    return child1, child2    


def pmx_crossover(parent1, parent2):
    n = len(parent1)
    child1 = [None] * n
    child2 = [None] * n
    
    i1, i2 = random.randint(0, len(parent1)-1), random.randint(0, len(parent1)-1)
    if i2 < i1:
        i1, i2 = i2, i1

    child1[i1:i2] = parent1[i1:i2]
    child2[i1:i2] = parent2[i1:i2]

    for i in range(n):
        if i1 <= i < i2:
            continue
        
        if parent2[i] in child1[i1:i2]:
            value = parent2[i]
            while value in child1[i1:i2]:
                idx = parent1.index(value)
                value = parent2[idx]
            child1[i] = value
        else:
            child1[i] = parent2[i]

        if parent1[i] in child2[i1:i2]:
            value = parent1[i]
            while value in child2[i1:i2]:
                idx = parent2.index(value)
                value = parent1[idx]
            child2[i] = value
        else:
            child2[i] = parent1[i]

    return child1, child2


def order_crossover(parent1, parent2):
    n = len(parent1)
    child1 = [None] * n
    child2 = [None] * n
    
    i1, i2 = random.randint(0, len(parent1)-1), random.randint(0, len(parent1)-1)
    if i2 < i1:
        i1, i2 = i2, i1

    child1[i1:i2] = parent1[i1:i2]
    child2[i1:i2] = parent2[i1:i2]

    temp1 = []
    temp2 = []

    for i in range(i2, i2 + n):
        idx = i % n

        if parent2[idx] not in child1[i1:i2]:
            temp1.append(parent2[idx])

        if parent1[idx] not in child2[i1:i2]:
            temp2.append(parent1[idx])

    j1 = 0
    j2 = 0
    for i in range(i2, i2 + n):
        idx = i % n
        if i1 <= idx < i2:
            continue
        child1[idx] = temp1[j1]
        child2[idx] = temp2[j2]

        j1 += 1
        j2 += 1

    return child1, child2

def genetic_algorithm(
    n,
    distances,
    nb_tours=100,
    max_gen=500,
    mutation_rate=0.1,
    crossover_fn=cycle_crossover,
    mutation_fn=displacement_mutation,
):
    populations = random_population(nb_tours, n)

    nb_generations = 0

    while nb_generations < max_gen:
        random_pop = random.sample(populations, 2)
        parent1 = random_pop[0]
        parent2 = random_pop[1]

        child1, child2 = crossover_fn(parent1, parent2)

        if mutation_rate > random.random():
            child1 = mutation_fn(child1)

        if mutation_rate > random.random():
            child2 = mutation_fn(child2)

        populations.append(child1)
        populations.append(child2)

        populations = sorted(populations, key= lambda tour : tour_length(tour, distances))[:nb_tours]

        nb_generations += 1

    return populations[0]

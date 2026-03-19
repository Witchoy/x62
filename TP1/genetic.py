import random as rd

def random_population(nb_tours, n):
    pop = []
    for i in range(nb_tours):
        temp = []
        for j in range(n):
            temp.append(rd.randrange(n))
        pop.append(temp)
    
    return pop

def displacement_mutation(tour):
    

def main():
    populations = random_population(3, 10)

    for i in range(3):
        print(populations[i])

    return 0

main()
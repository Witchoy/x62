import random as rd
import matplotlib.pyplot as plt
import math
import numpy as np

class city:
    def __init__(self):
        self.x = rd.random()
        self.y = rd.random()
    def print(self): 
        print("x: ", self.x, " y: ", self.y)

def init_cities(n): 
    cities = []
    for _ in range(n):
        cities.append(city())
    return cities
    
def draw_tour(cities, tour):
    if(not tour or not cities):
        return
    
    # Plot all cities
    x = [city.x for city in cities]
    y = [city.y for city in cities]
    plt.scatter(x, y, color='red', label='Cities')

    # Plot tour
    if tour:
        tour_indices = [i-1 for i in tour]
        if tour_indices[0] != tour_indices[-1]:
            tour_indices.append(tour_indices[0])
        tour_x = [cities[i].x for i in tour_indices]
        tour_y = [cities[i].y for i in tour_indices]
        plt.plot(tour_x, tour_y, color='blue', label='Tour')
    plt.legend()
    plt.grid()
    plt.show()

def distance(city1, city2):
    distance = math.sqrt((city1.x-city2.x)**2+(city1.y-city2.y)**2)
    return distance

def distance_matrix(cities):
    n = len(cities)
    matrix = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            matrix[i, j] = distance(cities[i], cities[j])
    return matrix

def tour_length(tour, distances):
    length = 0
    n = len(tour)
    for i in range(n):
        city_a = tour[i] - 1
        city_b = tour[(i + 1) % n] - 1
        length += distances[city_a, city_b]
    return length

def generate_all_tours(n):
    if n == 0:
        return [[]]
    tours = []
    for tour in generate_all_tours(n - 1):
        for i in range(len(tour) + 1):
            new_tour = tour[:i] + [n - 1] + tour[i:]
            tours.append(new_tour)
    return tours

def force_brute(distances):
    tours = generate_all_tours(len(distances))
    min_length = float('inf')
    best_tour = None
    for tour in tours:
        tl = tour_length(tour, distances)
        if tl < min_length:
            best_tour = tour
            min_length = tl
    return best_tour


def main():
    n = 10

    print("=" * 40)
    print(f"  Travelling Salesman Problem (n={n})")
    print("=" * 40)

    # Cities initialization
    cities = init_cities(n)
    print(f"\n{n} cities generated:")
    for i, c in enumerate(cities):
        print(f"  City {i+1:2d}: ({c.x:.4f}, {c.y:.4f})")

    # Tour initialization
    tour = list(range(1, n + 1))
    print(f"\nTour: {tour}")

    # Distance matrix
    distances_matrix = distance_matrix(cities)
    print("\nDistance matrix:")
    for i in range(n):
        for j in range(n):
            print(f"{distances_matrix[i, j]:.4f}", end=" ")
        print()

    # Tour length
    length = tour_length(tour, distances_matrix)
    print(f"\nTotal tour length: {length:.4f}")
    print("=" * 40)

    # Generate all tours
    all_tours = generate_all_tours(n)
    print(f"\nTotal number of tours: {len(all_tours)}")

    # Brute-force solution
    best_tour = force_brute(distances_matrix)
    best_length = tour_length(best_tour, distances_matrix)
    print(f"\nBest tour found: {best_tour}")
    print(f"Best tour length: {best_length:.4f}")

    # Show tour graph
    draw_tour(cities, tour)

main()
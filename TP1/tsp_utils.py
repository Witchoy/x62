"""
TP1 - Algorithmes génétiques
Travelling Salesman Problem (TSP) - Utility functions
"""

import math
import random
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

class city: 
    def __init__(self, x=None, y=None):
        self.x = x if x is not None else random.random()
        self.y = y if y is not None else  random.random()

    def __str__(self):
        return f"{self.x, self.y}"
    
    def __repr__(self):
        return f"{self.x, self.y}"


def init_cities(n):
    cities = []
    for i in range (n):
        cities.append(city())
    return cities


def draw_tour(cities, tour = None):
    xpoints = [city.x for city in cities]
    ypoints = [city.y for city in cities]
    
    if tour:
        xcycle = [cities[t-1].x for t in tour] + [cities[tour[0]-1].x]
        ycycle = [cities[t-1].y for t in tour] + [cities[tour[0]-1].y]
        plt.plot(xcycle, ycycle)

    plt.scatter(xpoints, ypoints, color = '#FF0000')
    plt.show()


def distance(city1, city2):
    return math.sqrt((city2.x - city1.x)**2 + (city2.y - city1.y)**2)


def distance_matrix(cities):
    matrix = [[0] * len(cities) for _ in range(len(cities))]

    for i in range(len(cities)):
        for j in range(i, len(cities)):
            d = distance(cities[i], cities[j])
            matrix[j][i] = d
            matrix[i][j] = d

    return matrix


def tour_length(tour, distances):
    length = 0

    for i in range(len(tour)-1):
        i1, i2 = tour[i]-1, tour[i+1]-1
        length += distances[i1][i2]
    
    length += distances[tour[-1]-1][tour[0]-1]

    return length


def generate_all_tours(n):
    if n == 1:
        return [[1]]
    
    smaller_tours = generate_all_tours(n-1)

    result = []

    for tour in smaller_tours:
        for i in range(len(tour) + 1):
            new_tour = tour[:i] + [n] + tour[i:]
            result.append(new_tour)
    
    return result


def force_brute(distances):
    n = len(distances)
    tours = generate_all_tours(n)
    min_distance = tour_length(tours[0], distances)
    best_tour = tours[0]

    for t in tours:
        d = tour_length(t, distances)
        if d < min_distance:
            min_distance = d
            best_tour = t
    return best_tour
    

def random_sample_search(n, sample_size, distances):
    samples = []

    for i in range(sample_size):
        samples.append(random.sample(range(1, n+1), n))

    best_sample = samples[0]
    min_distance = tour_length(best_sample, distances)

    for s in samples:
        d = tour_length(s, distances)
        if d < min_distance:
            min_distance = d
            best_sample = s

    return (best_sample, min_distance)
    

def nearest_neighbor(distances, start=0):
    n = len(distances)

    visited = [False] * n
    tour = []

    current_city = start
    visited[current_city] = True
    tour.append(current_city + 1)

    for _ in range(n-1):
        min_distance = float('inf')
        next_city = None

        for j in range(n):
            if visited[j]:
                continue
            if distances[current_city][j] < min_distance:
                min_distance = distances[current_city][j]
                next_city = j
        
        visited[next_city] = True
        tour.append(next_city + 1)
        current_city = next_city

    return tour
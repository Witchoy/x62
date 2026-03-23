from tsp_utils import *
from genetic_algorithm import *

p1 = [1, 2, 3, 4, 5]
p2 = [3, 5, 4, 2, 1]
c1, c2 = pmx_crossover(p1, p2)
print(sorted(c1))
print(sorted(c2))
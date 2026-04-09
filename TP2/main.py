"""
TP2 - Descente de gradient
Point d'entrée : tests et visualisations
"""

import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from gradient_descent import *
from linear_regression import *


# --- Section 1.1 : Parabole f(x) = x² ---
# TODO: tester gradient_descent avec diff_parabole, observer l'effet du learning_rate

# points = gradient_descent(diff_parabole, start=5.0, learning_rate=0.001)
# print("gradient_descent(diff_parabole, start=5.0, learning_rate=0.001)")
# print(points)

# --- Section 1.2 : Quartique g(x) = x⁴ + 3x³ - 4x ---
# TODO: tester gradient_descent avec diff_quartique, observer minima locaux vs global

# points = gradient_descent(diff_quartique, start=0.4, learning_rate=0.001)
# print("gradient_descent(diff_quartique, start=0.4, learning_rate=0.001)")
# print(points)

# points = gradient_descent(diff_quartique, start=-15.0, learning_rate=0.001)
# print("gradient_descent(diff_quartique, start=-15.0, learning_rate=0.001)")
# print(points)

# --- Section 1.3 : Fonction Gamma ---
# TODO: tester gradient_descent avec diff_gamma sur les réels > 0

points = gradient_descent(diff_gamma, start=1.5, learning_rate=0.01)
print(points[-1])

# --- Section 2.1 : Régression linéaire (données synthétiques) ---
u_1 = np.array([-1.2, 1.5, -0.9, 1.2])
v_1 = np.array([-1.1, 1.2, -0.6, 0.9])

# TODO: appeler lin_reg_descent, afficher la descente 3D et la droite de régression

u_2 = np.array([5, 15, 25, 35, 45, 55, 0, 30])
v_2 = np.array([5, 20, 14, 32, 28, 38, 6, 25])

# TODO: tester avec u_2, v_2 et observer la vitesse de convergence


# --- Section 2.2 : Données réelles (Folds5x2_pp.xlsx) ---
# TODO: charger les données avec pandas, normaliser, appliquer lin_reg_descent
# TODO: calculer R² pour PE/AT et V/RH


# --- Section 2.3 : DGS stochastique ---
# TODO: comparer sgd_lin_reg et lin_reg_descent en termes de vitesse de convergence

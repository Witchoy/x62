"""
TP2 - Descente de gradient
Core gradient descent algorithm and 1D test functions
"""

import math


# --- Section 1 : fonctions dérivées pour l'expérimentation en dimension 1 ---

def diff_parabole(x):
    """Dérivée de f(x) = x²"""
    return 2 * x


def diff_quartique(x):
    """Dérivée de g(x) = x⁴ + 3x³ - 4x"""
    return 4 * x**3 + 9 * x**2 - 4


def numerical_diff(f, x, h=1e-5):
    """Approximation numérique de f'(x) par différence finie centrée :
    f'(x) ≈ (f(x+h) - f(x-h)) / (2h)
    """
    pass


def diff_gamma(x):
    """Dérivée numérique de la fonction Gamma d'Euler en x,
    calculée via numerical_diff avec math.gamma
    """
    pass


# --- Algorithme principal ---

def gradient_descent(diff, start, learning_rate=0.1, n_iter=50, tolerance=1e-6):
    """Descente de gradient générique sur une fonction de dérivée `diff`.

    Paramètres
    ----------
    diff          : fonction calculant le gradient (ou la dérivée) au point courant
    start         : point de départ de l'algorithme
    learning_rate : taux d'apprentissage (amplitude du pas)
    n_iter        : nombre maximal d'itérations
    tolerance     : seuil d'arrêt sur la norme du déplacement

    Retourne la liste de tous les points visités durant la descente.
    """

    points_visités = [start]
    point_courant = start

    for i in range(n_iter):
        step = - diff(point_courant) * learning_rate
        point_courant += step
        points_visités.append(point_courant)
        if(abs(step) < tolerance):
            break

    return points_visités

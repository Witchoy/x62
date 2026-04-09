"""
TP2 - Descente de gradient
Linear regression via gradient descent (sections 2.1, 2.2, 2.3)
"""

import numpy as np


# --- Section 2.1 : moindres carrés ---

def mse(u, v, b):
    """Mean Squared Error entre les observations v et les prédictions b[0] + b[1]*u.

    u : array des xi
    v : array des yi
    b : [b0, b1] coefficients du modèle linéaire
    """
    pass


def ssr_gradient(u, v, b):
    """Gradient de la fonction de coût C = MSE/2 par rapport à b = [b0, b1].

    Retourne un vecteur [∂C/∂b0, ∂C/∂b1].
    Les formules analytiques sont données dans le sujet.
    """
    pass


def lin_reg_descent(u, v, learn_rate=0.1, n_iter=50, tolerance=1e-6):
    """Descente de gradient pour la régression linéaire.

    u, v         : données (arrays numpy des xi et yi)
    learn_rate   : taux d'apprentissage
    n_iter       : nombre maximal d'itérations
    tolerance    : seuil d'arrêt sur la norme du déplacement

    Retourne la suite des points [b0, b1] parcourus durant la descente.
    """
    pass


# --- Section 2.2 : coefficient de détermination ---

def R2(u, v, b):
    """Coefficient de détermination R² pour les données u, v
    et les coefficients de régression b = [b0, b1].

    R² = variance expliquée par le modèle / variance totale de v
    """
    pass


# --- Section 2.3 : descente de gradient stochastique ---

def sgd_lin_reg(u, v, learn_rate=0.1, n_iter=50, tolerance=1e-6, batch_size=1):
    """Descente de gradient stochastique (par lots) pour la régression linéaire.

    Même interface que lin_reg_descent, avec en plus :
    batch_size : taille des lots (batches) tirés aléatoirement à chaque itération.
                 batch_size=1  → DGS en ligne (online)
                 batch_size=n  → descente classique (batch complet)

    Un passage complet sur tous les lots constitue une époque (epoch).
    Retourne la suite des points [b0, b1] parcourus.
    """
    pass

import numpy as np
import pandas as pd
from scipy.stats import ttest_ind
from .selection_actions import selectionner_actions

def generer_portefeuilles_aleatoires(df, nb_portefeuilles=1000):
    """
    Génère des rendements aléatoires en simulant la sélection de portefeuilles aléatoires.

    Args:
        df (pd.DataFrame): DataFrame contenant les rendements des actions.
        nb_portefeuilles (int): Nombre de portefeuilles aléatoires à générer.

    Returns:
        np.array: Un tableau des rendements moyens simulés des portefeuilles aléatoires.
    """
    rendements_aleatoires = []

    for _ in range(nb_portefeuilles):
        # Sélectionner aléatoirement des actions et calculer le rendement moyen
        actions_aleatoires = df.sample(n=30, axis=1)  # Ajustez n selon le nombre d'actions à sélectionner
        rendement_moyen = actions_aleatoires.mean().mean()  # Calcule le rendement moyen des actions sélectionnées
        rendements_aleatoires.append(rendement_moyen)

    return np.array(rendements_aleatoires)


def evaluer_strategie(portefeuille_long, portefeuille_short):
    """
    Évalue et compare les performances des portefeuilles long et short.

    Args:
        portefeuille_long (pd.DataFrame): Le DataFrame représentant le portefeuille long.
        portefeuille_short (pd.DataFrame): Le DataFrame représentant le portefeuille short.
    """

    # Exemple de logique d'évaluation, à adapter selon vos besoins
    # Par exemple, calculer et afficher les rendements moyens des deux portefeuilles
    rendement_moyen_long = portefeuille_long['Score Global'].mean()
    rendement_moyen_short = portefeuille_short['Score Global'].mean()

    print(f"Rendement moyen du portefeuille long: {rendement_moyen_long}")
    print(f"Rendement moyen du portefeuille short: {rendement_moyen_short}")

    # Ajoutez ici d'autres analyses ou comparaisons nécessaires pour évaluer la stratégie


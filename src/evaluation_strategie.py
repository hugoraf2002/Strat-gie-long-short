# src/evaluation_strategie.py
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

    # S'assurer que le DataFrame contient une colonne pour les rendements
    if 'Rendement' not in df.columns:
        raise ValueError("Le DataFrame doit contenir une colonne 'Rendement'.")

    for _ in range(nb_portefeuilles):
        # Sélectionner aléatoirement des actions et calculer le rendement moyen
        rendement_moyen = df['Rendement'].sample(n=30).mean()  # Ajuster n=30 si nécessaire
        rendements_aleatoires.append(rendement_moyen)

    return np.array(rendements_aleatoires)

def evaluer_strategie(df):
    """
    Évalue la stratégie d'investissement en comparant ses rendements à ceux de portefeuilles aléatoires.
    
    Args:
        df (pd.DataFrame): DataFrame contenant les scores et les rendements des actions.
    """
    # Appliquer la stratégie d'investissement
    portefeuille_long, portefeuille_short = selectionner_actions(df)

    # Calculer le rendement moyen des portefeuilles
    # Supposons que 'Rendement' est la colonne de rendement dans les DataFrames retournés
    rendement_strategique = (portefeuille_long['Rendement'].mean() - portefeuille_short['Rendement'].mean())

    # Générer et comparer avec des rendements de portefeuilles aléatoires
    rendements_aleatoires = generer_portefeuilles_aleatoires(df)

    # Test t pour comparer les rendements
    t_stat, p_value = ttest_ind([rendement_strategique], rendements_aleatoires)

    print(f"Rendement moyen de la stratégie: {rendement_strategique}")
    print(f"P-value de la comparaison: {p_value}")

    if p_value < 0.05:
        print("La stratégie surperforme significativement les portefeuilles aléatoires.")
    else:
        print("La différence de performance n'est pas statistiquement significative.")

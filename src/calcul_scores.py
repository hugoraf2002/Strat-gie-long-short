import numpy as np

def calculer_score_momentum(rendements):
    """Calcule le score de momentum."""
    rendement_moyen = rendements.mean()
    return np.std(rendements - rendement_moyen)

def calculer_score_valeur(ratio_cours_valeur):
    """Calcule le score de valeur."""
    try:
        return 1 / float(ratio_cours_valeur)
    except ZeroDivisionError:
        return np.nan

def calculer_score_global(score_momentum, score_valeur):
    """Calcule le score global comme moyenne des scores momentum et valeur."""
    return (score_momentum + score_valeur) / 2

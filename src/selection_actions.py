# src/selection_actions.py
import pandas as pd
from .calcul_scores import calculer_score_momentum, calculer_score_valeur, calculer_score_global

def selectionner_actions(df):
    # Assurez-vous que df est le DataFrame correct avec les données attendues
    scores = pd.DataFrame(index=df.columns, columns=['Score Momentum', 'Score Valeur', 'Score Global'])
    for action in df.columns:
        rendements = df[action].dropna()  # Supposons que cela donne les rendements directement
        score_momentum = calculer_score_momentum(rendements[:-1])  # Excluez le dernier mois pour le calcul du momentum
        score_valeur = calculer_score_valeur(rendements.iloc[-1])  # Supposons que le dernier mois donne le ratio cours/valeur
        score_global = calculer_score_global(score_momentum, score_valeur)
        
        scores.loc[action, 'Score Momentum'] = score_momentum
        scores.loc[action, 'Score Valeur'] = score_valeur
        scores.loc[action, 'Score Global'] = score_global
    
    scores = scores.apply(pd.to_numeric, errors='coerce')
    portefeuille_long = scores.nlargest(15, 'Score Global')
    portefeuille_short = scores.nsmallest(15, 'Score Global')
    
    return portefeuille_long, portefeuille_short

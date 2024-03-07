from src.selection_actions import selectionner_actions
from src.evaluation_strategie import evaluer_strategie
import pandas as pd

def afficher_portefeuilles(portefeuille_long, portefeuille_short):
    """
    Affiche les détails des portefeuilles long et short.
    
    Args:
        portefeuille_long (pd.DataFrame): DataFrame des actions du portefeuille long.
        portefeuille_short (pd.DataFrame): DataFrame des actions du portefeuille short.
    """
    print("Portefeuille Long:")
    print(portefeuille_long)
    print("\nPortefeuille Short:")
    print(portefeuille_short)

# Exemple d'utilisation de la fonction :
# afficher_portefeuilles(portefeuille_long, portefeuille_short)


chemin_fichier_excel = 'DATA.xlsx'
df = pd.read_excel(chemin_fichier_excel, engine='openpyxl', index_col=0)

portefeuille_long, portefeuille_short = selectionner_actions(df)


afficher_portefeuilles(portefeuille_long, portefeuille_short)

evaluer_strategie(portefeuille_long, portefeuille_short)

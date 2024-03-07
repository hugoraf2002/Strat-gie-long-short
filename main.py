from src.selection_actions import selectionner_actions
from src.evaluation_strategie import evaluer_strategie
import pandas as pd

chemin_fichier_excel = 'DATA.xlsx'
df = pd.read_excel(chemin_fichier_excel, engine='openpyxl', index_col=0)

portefeuille_long, portefeuille_short = selectionner_actions(df)
evaluer_strategie(portefeuille_long, portefeuille_short)

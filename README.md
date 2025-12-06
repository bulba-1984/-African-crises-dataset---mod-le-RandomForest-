
# African Crises Dataset - Modèle RandomForest

## Description du projet
Ce projet utilise l'ensemble de données Kaggle sur les crises systémiques, bancaires et inflationnistes en Afrique pour prédire l'apparition d'une crise systémique à l'aide d'un modèle Random Forest.

## Contenu du dataset
- 13 pays africains (Algérie, Angola, République centrafricaine, Côte d’Ivoire, Égypte, Kenya, Maurice, Maroc, Nigéria, Afrique du Sud, Tunisie, Zambie, Zimbabwe)
- Période : 1860 - 2014
- Colonnes : country_number, country_code, country, year, systemic_crisis, exch_usd, domestic_debt_in_default, sovereign_external_debt_default, gdp_weighted_default, inflation_annual_cpi, independence, currency_crises, inflation_crises, banking_crisis

## Étapes réalisées
1. Import et exploration des données
2. Profiling avec pandas_profiling
3. Gestion des valeurs manquantes et doublons
4. Encodage des variables catégorielles
5. Sélection des features et de la variable cible
6. Séparation train/test
7. Entraînement du modèle Random Forest
8. Évaluation des performances avec Accuracy, Confusion Matrix et Classification Report

## Résultats
- Accuracy: 1.0
- Confusion Matrix:
  [[195  0]
   [  0 17]]
- Classification Report: Precision, Recall et F1-score parfaits (1.0)

## Instructions pour exécuter le projet
1. Cloner le dépôt
2. Créer un environnement virtuel et installer les dépendances
3. Lancer [1;34mUpgrade to ydata-sdk[0m
Improve your data and profiling with ydata-sdk, featuring data quality scoring, redundancy detection, outlier identification, text validation, and synthetic data generation.
Register at https://ydata.ai/register
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1059 entries, 0 to 1058
Data columns (total 14 columns):
 #   Column                           Non-Null Count  Dtype  
---  ------                           --------------  -----  
 0   country_number                   1059 non-null   int64  
 1   country_code                     1059 non-null   object 
 2   country                          1059 non-null   object 
 3   year                             1059 non-null   int64  
 4   systemic_crisis                  1059 non-null   int64  
 5   exch_usd                         1059 non-null   float64
 6   domestic_debt_in_default         1059 non-null   int64  
 7   sovereign_external_debt_default  1059 non-null   int64  
 8   gdp_weighted_default             1059 non-null   float64
 9   inflation_annual_cpi             1059 non-null   float64
 10  independence                     1059 non-null   int64  
 11  currency_crises                  1059 non-null   int64  
 12  inflation_crises                 1059 non-null   int64  
 13  banking_crisis                   1059 non-null   object 
dtypes: float64(3), int64(8), object(3)
memory usage: 116.0+ KB
None
   country_number country_code  ... inflation_crises  banking_crisis
0               1          DZA  ...                0          crisis
1               1          DZA  ...                0       no_crisis
2               1          DZA  ...                0       no_crisis
3               1          DZA  ...                0       no_crisis
4               1          DZA  ...                0       no_crisis

[5 rows x 14 columns]
Accuracy: 1.0
Confusion Matrix:
 [[195   0]
 [  0  17]]
Classification Report:
               precision    recall  f1-score   support

           0       1.00      1.00      1.00       195
           1       1.00      1.00      1.00        17

    accuracy                           1.00       212
   macro avg       1.00      1.00      1.00       212
weighted avg       1.00      1.00      1.00       212

## Auteur
⚓ YFZ 2025 Bulba

import pandas as pd
from pandas_profiling import ProfileReport
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Charger les données
df = pd.read_csv('African_crises_dataset.csv')
print(df.info())
print(df.head())

# Profiling pandas
profile = ProfileReport(df, title='Profiling African Crises Dataset', explorative=True)
profile.to_file('African_crises_profiling.html')

# Gestion valeurs manquantes et doublons
df = df.drop_duplicates()
df = df.fillna(df.median(numeric_only=True))

# Encodage des variables catégorielles
df = pd.get_dummies(df, drop_first=True)

# Définir cible et caractéristiques
# Remplacer 'systemic_crisis' par le nom exact de la colonne cible
y = df['systemic_crisis']
X = df.drop('systemic_crisis', axis=1)

# Division train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modèle Random Forest
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Prédiction et évaluation
y_pred = clf.predict(X_test)
print('Accuracy:', accuracy_score(y_test, y_pred))
print('Confusion Matrix:\n', confusion_matrix(y_test, y_pred))
print('Classification Report:\n', classification_report(y_test, y_pred))

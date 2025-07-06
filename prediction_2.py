from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

import os
import json
import pandas as pd

# Répertoire contenant les fichiers JSON
json_dir = 'json_Constructor'

data = []

# Charger tous les fichiers
for filename in os.listdir(json_dir):
    if filename.startswith("constructor_summary_") and filename.endswith(".json"):
        with open(os.path.join(json_dir, filename), 'r') as f:
            season_data = json.load(f)
            for constructor in season_data:
                # On crée une ligne avec les features qu'on veut
                row = {
                    'year': constructor['year'],
                    'constructor': constructor['constructor'],
                    'total_points': constructor['total_points'],
                    'wins': constructor['wins'],
                    'avg_qualifying_pos': constructor['avg_qualifying_pos'],
                    'avg_finish_pos': constructor['avg_finish_pos'],
                    'dnf_count': constructor['dnf_count'],
                }
                data.append(row)

# Convertir en DataFrame
df = pd.DataFrame(data)

# Trier par année et points pour obtenir la position (championnat)
df['rank'] = df.groupby('year')['total_points'].rank(method='min', ascending=False)

# X = toutes les features sauf 'constructor', 'year', et 'rank'
X = df[['total_points', 'wins', 'avg_qualifying_pos', 'avg_finish_pos', 'dnf_count']]
y = df['rank']



# Exemple (en supposant X et y prêts)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

models = {
    "Random Forest": RandomForestClassifier(),
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Gradient Boosting": GradientBoostingClassifier(),
    "Linear SVM": SVC(kernel='linear')
}

for name, model in models.items():
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    print(f"\n{name} accuracy:", accuracy_score(y_test, preds))
    print(classification_report(y_test, preds))

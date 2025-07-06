import pandas as pd
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, accuracy_score
import matplotlib.pyplot as plt

# === Chargement des données ===
df = pd.read_csv("C:/Users/romai/Documents/B3/FF11/data/Data_final 1.csv", sep=";")

# === Features disponibles AVANT saison (sans triche) ===
features = ['avg_driver_points', 'avg_grid_position', 'dnf_count']

# Nettoyage
df = df.dropna(subset=features + ['target', 'year', 'name'])
df = df.sort_values(by='year')
years = sorted(df['year'].unique())

# === Modèles à comparer ===
models = {
    "Random Forest": RandomForestClassifier(random_state=42),
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Gradient Boosting": GradientBoostingClassifier(random_state=42),
    "SVM (linéaire)": SVC(kernel='linear', probability=True)
}

# === Prédictions saison par saison ===
comparative_results = []
conf_matrices = {name: {"y_true": [], "y_pred": []} for name in models.keys()}

print("🔁 Prédictions saison par saison (sans triche) :\n")

for year in years:
    if year in (2024, min(years)):
        continue


    train_df = df[df['year'] < year]
    test_df = df[df['year'] == year]

    if train_df.empty or test_df.empty:
        continue

    X_train = train_df[features]
    y_train = train_df['target']
    X_test = test_df[features]

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    true_team = test_df.loc[test_df['target'] == 1, 'name'].values
    real_team = true_team[0] if len(true_team) > 0 else "❌ Aucune"

    row_result = {"Année": int(year), "Réel": real_team}

    for model_name, model in models.items():
        model.fit(X_train_scaled, y_train)
        y_pred = model.predict(X_test_scaled)
        y_proba = model.predict_proba(X_test_scaled)[:, 1] if hasattr(model, "predict_proba") else y_pred

        test_df_copy = test_df.copy()
        test_df_copy['prediction'] = y_pred
        test_df_copy['proba'] = y_proba

        if (test_df_copy['prediction'] == 1).any():
            predicted_team = test_df_copy.loc[test_df_copy['prediction'] == 1, 'name'].values[0]
        else:
            predicted_team = test_df_copy.sort_values(by='proba', ascending=False).iloc[0]['name']

        row_result[model_name] = predicted_team
        conf_matrices[model_name]["y_true"].append(1 if real_team == predicted_team else 0)
        conf_matrices[model_name]["y_pred"].append(1)

    comparative_results.append(row_result)

from utils.confusion_utils import get_confusion_image

confusion_images = {}

for model_name, data in conf_matrices.items():
    image = get_confusion_image(data["y_true"], data["y_pred"], model_name)
    confusion_images[model_name] = image

# === Affichage du tableau ===
results_df = pd.DataFrame(comparative_results)
print("\n📊 Résultats comparés saison par saison :\n")
print(results_df.to_string(index=False))

# === Précision globale par modèle ===
print("\n📈 Précision globale par modèle :")
accuracies = {}
for model_name, data in conf_matrices.items():
    acc = accuracy_score(data["y_true"], data["y_pred"])
    accuracies[model_name] = round(acc * 100, 2)
    print(f"{model_name}: {accuracies[model_name]} %")

# === Matrices de confusion ===
print("\n🧩 Matrices de confusion :\n")
for model_name, data in conf_matrices.items():
    cm = confusion_matrix(data["y_true"], data["y_pred"], labels=[0, 1])
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Faux", "Vrai"])
    disp.plot(cmap="Blues")
    plt.title(f"Matrice de confusion : {model_name}")
    plt.xlabel("Prédit")
    plt.ylabel("Réel")
    plt.tight_layout()
    plt.show()

# === Prédiction simulée pour 2024 ===
print("\n🔮 Simulation du champion 2024 (en utilisant données jusqu'à 2023) :\n")

train_df = df[df['year'] < 2024]
test_df_2024 = df[df['year'] == 2023].copy()
test_df_2024['year'] = 2024
test_df_2024 = test_df_2024.drop(columns=['target'])

X_train = train_df[features]
y_train = train_df['target']
X_test = test_df_2024[features]

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

predictions_2024 = []

for model_name, model in models.items():
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    y_proba = model.predict_proba(X_test_scaled)[:, 1] if hasattr(model, "predict_proba") else y_pred

    test_df_2024['prediction'] = y_pred
    test_df_2024['proba'] = y_proba

    if (test_df_2024['prediction'] == 1).any():
        predicted_team = test_df_2024.loc[test_df_2024['prediction'] == 1, 'name'].values[0]
    else:
        predicted_team = test_df_2024.sort_values(by='proba', ascending=False).iloc[0]['name']

    print(f"🏁 {model_name} prédit comme champion en 2024 : **{predicted_team}**")
    predictions_2024.append({
        "Modèle": model_name,
        "Champion prédit 2024": predicted_team
    })
    # Enregistre les résultats pour l'utiliser dans l'app Dash
results_df.to_csv("data/predictions_summary.csv", index=False)
pred_2024_df = pd.DataFrame(predictions_2024)
predicted_2024 = {
    row["Modèle"]: [row["Champion prédit 2024"]]
    for _, row in pred_2024_df.iterrows()
}
print("\n📢 Résumé des prédictions pour 2024 :")
print(pred_2024_df.to_string(index=False))

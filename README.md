# 🎯 Recommandeur de Carrière - *IA*

Une application intelligente de **recommandation de carrière** basée sur le **machine learning**, avec une interface conviviale construite avec **Tkinter**.

> Trouvez votre voie professionnelle en fonction de vos intérêts, compétences et niveau d'études.

---

## 🗂️ Contenu du projet

- `data.csv` : Données d'exemple (intérêts, compétences, études, carrière).
- `train_model.py` : Entraînement du modèle (Random Forest).
- `recommender.py` : Interface graphique utilisateur.
- `model.pkl` & encodeurs (`*.pkl`) : Fichiers générés à l'entraînement.
- `requirements.txt` : Dépendances nécessaires au projet.

---

## 🚀 Fonctionnalités clés

- 🔍 **Analyse personnalisée** selon vos réponses.
- 🧠 **Prédiction intelligente** grâce à un modèle ML performant.
- 🖥️ **Interface utilisateur simple et intuitive** avec Tkinter.
- 📈 **Réutilisation rapide du modèle** grâce aux fichiers sauvegardés (`.pkl`).
- 🔄 Possibilité de tester plusieurs combinaisons d’intérêts/compétences.

---

## 🧪 Exemple d'utilisation

- 💬 Intérêts : Technologie
- 🧰 Compétences : Programmation
- 🎓 Niveau d'études : Licence
- 🎯 Résultat suggéré : Ingénieur logiciel
---

## ⚙️ Comment ça marche ?

### Le script `train_model.py` :
- Entraîne un modèle `RandomForestClassifier` sur les données `data.csv`.
- Encode les données catégorielles avec `LabelEncoder`.
- Sauvegarde le modèle et les encodeurs (`*.pkl`) avec `joblib`.

### Le fichier `recommender.py` :
- Charge le modèle et les encodeurs.
- Affiche une interface graphique (via **Tkinter**).
- Prédit une carrière à partir des réponses de l’utilisateur.

---

## 🧬 Technologies utilisées

- **Python** – Langage principal.
- **Tkinter** – Pour créer l'interface graphique.
- **pandas** – Manipulation de données.
- **scikit-learn** – Entraînement du modèle ML (Random Forest).
- **joblib** – Sauvegarde/chargement du modèle et des encodeurs.

---

## 📦 Dépendances

Le projet repose sur les bibliothèques Python suivantes :

- [pandas](https://pandas.pydata.org/) – manipulation et analyse de données 🐼  
- [scikit-learn](https://scikit-learn.org/) – algorithmes de machine learning 🧠  
- [tkinter](https://docs.python.org/3/library/tkinter.html) – interface graphique avec Tk 🖼️  
- [joblib](https://joblib.readthedocs.io/) – sauvegarde et chargement du modèle ML 💾  

➡️ Toutes ces dépendances sont listées dans [requirements.txt](requirements.txt) pour une installation rapide.

---

## ❤️ Contribuer

Les contributions sont les bienvenues !  
💡 Que ce soit pour améliorer le modèle, enrichir l’interface ou ajouter des carrières : vos idées comptent !

---

## 📬 Contact

Pour toute question ou suggestion :

- 📧 **Email** : *lnantenaina78@gmail.com*  
- 🐙 **GitHub** : [github.com/Lovaxcoding](https://github.com/Lovaxcoding)

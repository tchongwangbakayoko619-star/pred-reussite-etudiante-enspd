# 🎓 Prédiction de la Réussite Académique à l'ENSPD

Optimisation de la gestion académique et prédiction de la réussite étudiante à l’ENSPD grâce au **Machine Learning**.  
Ce projet combine rigueur scientifique et innovation pédagogique pour anticiper les risques d’échec et proposer des recommandations personnalisées.

---

## 🚀 Objectifs du projet
- Identifier les **facteurs clés** influençant la réussite (sociaux, académiques et comportementaux).  
- Concevoir et implémenter des modèles de prédiction (*Régression Logistique* et *Arbre de Décision*).  
- Comparer les performances des modèles avec des métriques robustes (Accuracy, Precision, Recall, F1-score).  
- Déployer une **application web intuitive** avec Flask pour une utilisation en temps réel.  

---

## 🛠️ Particularité du projet
👉 Les modèles ont été **développés entièrement *from scratch***, sans utiliser de librairies de haut niveau comme scikit-learn pour l’entraînement.  
- Implémentation manuelle de la **descente de gradient**.  
- Calcul explicite de la **fonction de coût (log-loss)** et de sa convergence.  
- Construction d’un **Arbre de Décision** avec critères d’entropie et de gain d’information codés à la main.  
- Standardisation et encodage des variables réalisés manuellement pour garantir la transparence et la reproductibilité.  

Cette approche assure une meilleure compréhension des mécanismes internes et une maîtrise totale du pipeline de modélisation.  

---

## 📂 Structure du dépôt
projet/
# Scripts Python (prétraitement, modèles, API Flask)
# Jeux de données (réels + synthétiques)
# Rapport académique et annexes
├── templates/          # Interfaces HTML pour l’application web
├── requirements.txt     # Librairies Python nécessaires
├── .gitignore          # Fichiers ignorés (venv, pycache, etc.)
└── README.md            # Présentation du projet

---


---

## 🧑‍💻 Technologies utilisées
- **Python** (pandas, matplotlib, seaborn)  
- **Flask** (déploiement web)  
- **SQLite3** (base de données légère)  
- **Git & GitHub** (gestion de version et collaboration)  

---

## 📊 Résultats principaux
- **Modèle retenu** : Régression Logistique *from scratch* (robustesse et interprétabilité).  
- **Précision globale** : ~94% sur le dataset final.  
- **Facteurs les plus influents** :  
  - Taux de présence aux cours  
  - Heures d’étude quotidiennes  
  - Implication dans les travaux de groupe  
  - Interaction avec les enseignants  
  - Accès aux ressources pédagogiques  

---

## 🌐 Déploiement
Le modèle est intégré dans une **application web Flask** :  
- Interface simple et intuitive pour les étudiants et encadreurs.  
- Prédiction en temps réel avec recommandations personnalisées.  
- Exemple :  
  - Entrée : taux de présence = 75%, heures d’étude = 2h/jour  
  - Sortie : probabilité de réussite = **92.02%** 🎉  

---

## 📖 Références
- Njongwa Yepnga, N. (2023). *Programmation avec Python: Analyse de données et Data visualisation*. LeCoinStat.  
- LeCoinStat – [Chaîne YouTube](https://www.youtube.com/@LeCoinStat/playlists) (vulgarisation Data Science).  
- Hastie, T., Tibshirani, R., Friedman, J. (2009). *The Elements of Statistical Learning*. Springer.  

---

## 👨‍🎓 Auteurs
Projet réalisé par un **groupe d’étudiants ENSPD** en filière *Sciences des Données et Intelligence Artificielle*,  
sous la supervision de **Mme …**.  

---

## 🏆 Remerciements
- Corps enseignant et administratif de l’ENSPD.  
- Communauté **LeCoinStat** pour les ressources pédagogiques.  
- Microsoft Copilot pour l’assistance dans la génération de données synthétiques et la rédaction académique.  


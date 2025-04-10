# Ouest-France-streamlit


# Analyse des tendances et des sentiments dans les titres de presse RSS d'Ouest-France

Ce projet a pour objectif d'analyser les titres des flux RSS de différents domaines d'actualité fournis par Ouest-France. À l'aide de l'analyse de sentiment et de la visualisation des données, il permet d'identifier la répartition des titres selon leur tonalité (anxiogène, positive ou neutre). 

L'application permet à l'utilisateur de sélectionner un flux RSS parmi plusieurs catégories proposées (comme "Les Unes", "France et Monde", "Sport") et d'obtenir une analyse détaillée des titres publiés, avec une répartition des sentiments dans le temps. De plus, une option permet d'analyser l'ensemble des titres de plusieurs flux RSS pour obtenir une vue d'ensemble.

Le projet utilise la bibliothèque **ac0hik/Sentiment_Analysis_French**, qui est spécialement conçue pour effectuer une analyse de sentiment sur des textes en français. Cette bibliothèque permet de catégoriser chaque titre comme positif, négatif ou neutre, en tenant compte des spécificités du langage français.

**Technologies utilisées :**
- Python
- Streamlit pour l'interface web
- Matplotlib pour les graphiques interactifs
- Requests pour la récupération des flux RSS
- Analyse de sentiment avec **ac0hik/Sentiment_Analysis_French** (modèle d'analyse de sentiment en français)

**Fonctionnalités principales :**
- Récupération des titres à partir des flux RSS d'Ouest-France.
- Analyse de sentiment des titres à l'aide de la bibliothèque **ac0hik/Sentiment_Analysis_French**.
- Visualisation des résultats sous forme de graphiques interactifs avec **Streamlit**.
- Sélection d'un flux RSS spécifique ou de tous les flux combinés pour une analyse générale des titres.
- Répartition des titres en catégories (anxiogène, positif, neutre) et affichage de ces informations sous forme de graphiques.

## Installation

1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/piTibo/Ouest-France-streamlit.git
   ```

2. Accédez au dossier du projet :
   ```bash
   cd Ouest-France-streamlit
   ```

3. Créez un environnement virtuel et activez-le :
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # macOS/Linux
   ```

4. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

5. Lancez l'application Streamlit :
   ```bash
   streamlit run app.py
   ```

L'application s'ouvrira dans votre navigateur local, et vous pourrez analyser les titres des flux RSS d'Ouest-France.

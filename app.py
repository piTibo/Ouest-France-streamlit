import streamlit as st
import feedparser
import matplotlib.pyplot as plt
from transformers import pipeline

# Fonction pour récupérer les titres des articles depuis un flux RSS
def reccup_titres_rss(url):
    feed = feedparser.parse(url)
    titres = [entry.title for entry in feed.entries]
    return titres

# Analyser les sentiments des titres
def analyse_sentiment(titres):
    sentiment_analyzer = pipeline("sentiment-analysis", model="ac0hik/Sentiment_Analysis_French")
    resultat = {'negative': 0, 'positive': 0, 'neutral': 0}
    for titre in titres:
        sentiment = sentiment_analyzer(titre)
        label = sentiment[0]['label']
        if label == 'negative':
            resultat['negative'] += 1
        elif label == 'positive':
            resultat['positive'] += 1
        else:
            resultat['neutral'] += 1
    return resultat

# URLs des flux RSS de Ouest-France
rss_urls = {
    "Les Unes": "https://www.ouest-france.fr/rss/une",
    "France et Monde": "https://www.ouest-france.fr/rss/france",
    "Sport": "https://www.ouest-france.fr/rss/sport"
}

# Interface Streamlit
st.title("Analyse des titres de Ouest-France")
st.sidebar.title("Choisir un flux RSS")
flux_choisi = st.sidebar.selectbox("Sélectionner un flux RSS", list(rss_urls.keys()) + ["Tous les flux"])

# Fonction pour récupérer les titres des trois flux RSS
def recuperer_titres_complets():
    titres_complets = []
    for flux in rss_urls.values():
        titres_complets.extend(reccup_titres_rss(flux))  # Ajouter les titres de chaque flux
    return titres_complets

# Récupérer et analyser les titres du flux choisi
if flux_choisi == "Tous les flux":
    titres = recuperer_titres_complets()  # Combiner tous les titres des flux
else:
    titres = reccup_titres_rss(rss_urls[flux_choisi])

resultat_sentiment = analyse_sentiment(titres)

# Affichage des résultats
st.write(f"Nombre de titres analysés pour {flux_choisi}: {len(titres)}")
st.write(f"Titres anxiogènes: {resultat_sentiment['negative']}")
st.write(f"Titres positifs: {resultat_sentiment['positive']}")
st.write(f"Titres neutres: {resultat_sentiment['neutral']}")

# Graphique de répartition des sentiments
labels = ["Anxiogènes", "Positifs", "Neutres"]
sizes = [resultat_sentiment['negative'], resultat_sentiment['positive'], resultat_sentiment['neutral']]

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(labels, sizes, color=['red', 'green', 'gray'])

# Affichage des chiffres au-dessus des barres
for i, v in enumerate(sizes):
    ax.text(i, v + 0.2, str(v), ha='center', fontsize=12)

# Configurer la grille horizontale
ax.yaxis.grid(True, which='both', linestyle='--', linewidth=0.5)

# Ajouter des ticks pour l'axe y tous les 5
ax.set_yticks(range(0, max(sizes) + 5, 5))  # Ajuster la plage pour une meilleure visualisation

# Titre et labels du graphique
plt.title(f"Répartition des sentiments pour le flux RSS: {flux_choisi}")
plt.xlabel("Type de titre")
plt.ylabel("Nombre de titres")

# Afficher le graphique avec Streamlit
st.pyplot(fig)
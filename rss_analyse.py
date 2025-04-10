import feedparser
import matplotlib
matplotlib.use('Qt5Agg')
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
        label = sentiment[0]['label'].lower()  # "negative", "positive", "neutral"
        if label in resultat:
            resultat[label] += 1
    return resultat

# URLs des flux RSS de Ouest-France
rss_urls = [
    "https://www.ouest-france.fr/rss/une",
    "https://www.ouest-france.fr/rss/france",
    "https://www.ouest-france.fr/rss/sport"
]

# Récupérer et analyser les titres des trois flux RSS
liste_titres = []
liste_sentiments = {'negative': 0, 'positive': 0, 'neutral': 0}

for url in rss_urls:
    titres = reccup_titres_rss(url)
    sentiments = analyse_sentiment(titres)
    liste_titres.extend(titres)
    liste_sentiments['negative'] += sentiments['negative']
    liste_sentiments['positive'] += sentiments['positive']
    liste_sentiments['neutral'] += sentiments['neutral']

# Visualisation des sentiments (nombre de titres par sentiment)
labels = ['Anxiogènes (negative)', 'Positifs (positive)', 'Neutres (neutral)']
values = [liste_sentiments['negative'], liste_sentiments['positive'], liste_sentiments['neutral']]

# Afficher les résultats
print(f"Nombre de titres : {len(liste_titres)}")
print(f"Nombre de titres anxiogènes : {liste_sentiments['negative']}")
print(f"Nombre de titres positifs : {liste_sentiments['positive']}")
print(f"Nombre de titres neutres : {liste_sentiments['neutral']}")

# Visualisation avec matplotlib
plt.figure(figsize=(10, 6))
bars = plt.bar(labels, values, color=['red', 'green', 'blue'])

# Afficher les chiffres au-dessus des barres
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.5, int(yval), ha='center', va='bottom')

# Ajouter la grille horizontale
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Ajuster la graduation verticale tous les 5
plt.yticks(range(0, max(values) + 5, 5))

# Ajouter les titres et labels
plt.title("Répartition des titres anxiogènes, positifs et neutres")
plt.xlabel("Type de titre")
plt.ylabel("Nombre de titres")

# Afficher le graphique
plt.show()

plt.savefig('graphique.png')
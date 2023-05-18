import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# download necessary resources
nltk.download('vader_lexicon')

# load the texts
texts = ["I love working with Python!", 
         "The weather is terrible today.",
         "This movie is absolutely amazing!",
         "I don't like this restaurant at all."]

# create a SentimentIntensityAnalyzer object
analyzer = SentimentIntensityAnalyzer()

# loop through the texts and get the sentiment of each text
for text in texts:
    sentiment = analyzer.polarity_scores(text)
    print("Text: ", text)
    print("Sentiment Score: ", sentiment['compound'])
    print("\n")

import json
import random
import nltk
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

nltk.download('punkt')

# Load intents
with open("intents.json") as f:
    data = json.load(f)

# Prepare training data
X = []
y = []
for intent in data["intents"]:
    for pattern in intent["patterns"]:
        X.append(pattern)
        y.append(intent["tag"])

# Text preprocessing and vectorization
vectorizer = CountVectorizer(tokenizer=nltk.word_tokenize)
X_vec = vectorizer.fit_transform(X)

# Train model
model = MultinomialNB()
model.fit(X_vec, y)

# Save model and vectorizer
with open("chatbot_model.pkl", "wb") as f:
    pickle.dump(model, f)
with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("Model trained and saved!")

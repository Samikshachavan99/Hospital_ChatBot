import json
import random
import pickle
import nltk

nltk.download('punkt')

# Load saved model and vectorizer
with open("chatbot_model.pkl", "rb") as f:
    model = pickle.load(f)
with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)
with open("intents.json") as f:
    intents = json.load(f)

# Predict intent
def get_intent(text):
    X = vectorizer.transform([text])
    intent = model.predict(X)[0]
    return intent

# Get response
def get_response(intent):
    for i in intents["intents"]:
        if i["tag"] == intent:
            return random.choice(i["responses"])

# Chat loop
print("Chatbot is running! (type 'quit' to exit)")
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break
    intent = get_intent(user_input)
    response = get_response(intent)
    print("Bot:", response)

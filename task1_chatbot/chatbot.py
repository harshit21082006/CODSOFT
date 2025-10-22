# chatbot.py
import json
import random

# Load intents
with open("intents.json") as file:
    data = json.load(file)

def get_response(msg):
    msg = msg.lower()
    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            if msg == pattern.lower():
                return random.choice(intent["responses"])
    # fallback response
    fallback_intent = next((i for i in data["intents"] if i["tag"]=="fallback"), None)
    return random.choice(fallback_intent["responses"]) if fallback_intent else "I don't understand."

import json
import random

# Load intents
with open("intents.json") as file:
    data = json.load(file)

def get_response(user_input):
    user_input = user_input.lower()  # Convert input to lowercase
    
    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            pattern_lower = pattern.lower()
            # Check if the pattern is anywhere in the user input
            if pattern_lower in user_input:
                return random.choice(intent["responses"])
    
    # Default response if nothing matches
    return "Sorry, I didn't understand that. Can you rephrase?"

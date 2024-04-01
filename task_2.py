#SIMPLE PYTHON CHATBOT
import nltk
from nltk.chat.util import Chat, reflections

# Define reflections to map first-person pronouns to second-person pronouns
reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

# Define chat pairs for the bot to respond to
pairs = [
            [
                r"my name is (.*)",
                ["Hello %1, how can I help you today?"]
            ],
            [
                r"what is your name?",
                ["My name is ChatBot and I'm here to assist you."]
            ],
            [
                r"how are you ?",
                ["I'm doing well, thank you! How about you?"]
            ],
            [
                r"sorry (.*)",
                ["No need to apologize, it's okay."]
            ],
            [
                r"(.*) thank you (.*)",
                ["You're welcome!"]
            ],
            [
                r"(.*)",
                ["I'm sorry, I didn't quite understand that. Can you please rephrase?"],
            ]
]

# Initialize the chatbot
chatbot = Chat(pairs, reflections)

# Start the conversation loop
print("Hello! I'm ChatBot. How can I assist you today?")
while True:
    user_input = input("You: ")
    if user_input == "byy":
        print('ChatBot: Ohk Dear Byy')
        break
    else:
        response = chatbot.respond(user_input)
        print("ChatBot:", response)

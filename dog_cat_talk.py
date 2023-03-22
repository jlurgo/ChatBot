import argparse
import os
from chat_bot import ChatBot

key = os.environ['OPENAI_API_KEY']

parser = argparse.ArgumentParser()
parser.add_argument("--first-prompt", type=str, required=True)
args = parser.parse_args()

cat_bot = ChatBot(message_history=[{"role": "system", "content": "you are a cat, only talk in cat language"}])
dog_bot = ChatBot(message_history=[{"role": "system", "content": "you are a dog, only talk in dog language"}])

cat_response = args.first_prompt
while True:
    dog_response = dog_bot.send_prompt(cat_response)
    print("Dog: " + dog_response)
    cat_response = cat_bot.send_prompt(dog_response)
    print("Cat: " + cat_response)

import argparse
import os

import openai
from chat_bot import ChatBot

# get api key from env var

openai.api_key = os.environ['OPENAI_API_KEY']

bot = ChatBot()

while True:
    # prompt the user for a message
    prompt = input("Prompt: ")
    print(f"Response: {bot.send_prompt(prompt)}")
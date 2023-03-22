import argparse
import os
from completion_chat_bot import CompletionChatBot

key = os.environ['OPENAI_API_KEY']

parser = argparse.ArgumentParser()
parser.add_argument("--prompt", type=str, required=True)
parser.add_argument("--file_name", type=str, required=True)
args = parser.parse_args()
bot = CompletionChatBot(key, args.file_name)


print(bot.send_prompt(args.prompt))
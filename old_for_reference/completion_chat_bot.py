import openai
import os

class CompletionChatBot:
    def __init__(self, api_key, model_engine, history_file):
        openai.api_key = api_key
        self.model_engine = model_engine
        self.history_file = history_file
        self.conversation_history = ""

        # Load previous conversation history from file, if it exists
        if os.path.exists(history_file):
            with open(history_file, "r") as f:
                self.conversation_history = f.read()

    def send_prompt(self, prompt):
        prompt_with_history = self.conversation_history + "Prompt: " + prompt

        # Send the prompt to the OpenAI API and retrieve the response
        response = openai.Completion.create(
            engine=self.model_engine,
            prompt=prompt_with_history,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )

        # Append the new response to the conversation history
        self.conversation_history += "Prompt: " + prompt + "\nResponse: " + response.choices[0].text + "\n"

        # Write the updated conversation history to the file, to save it
        with open(self.history_file, "w") as f:
            f.write(self.conversation_history)

        # Return the response
        return response.choices[0].text

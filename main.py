from openai import OpenAI
from ansi_codes import *
import os

def get_user_message():
    return input()

class Agent:

    model = "tngtech/deepseek-r1t-chimera:free"

    def __init__(self, client: OpenAI, get_user_message):
        self.client = client
        self.get_user_message = get_user_message

    def run(self):
        conversation = []
        # system prompt
        conversation.append({
            "role": "system",
            "content": "respond succinctly"
            })

        print("Chat with " + self.model + " (use ctrl-c to quit)")

        while True:
            print(ANSI_BLUE + "You" + ANSI_END + ": ", end="")
            user_input = self.get_user_message()

            conversation.append({
                "role": "user",
                "content": user_input
                })

            message = self.run_inference(conversation)
            conversation.append({
                "role": "assistant",
                "content": message
                })

            print(ANSI_ORANGE + "Model" + ANSI_END + ": ", end="")
            print(message)

    def run_inference(self, conversation):
        response =  self.client.chat.completions.create(
                model=self.model,
                messages=conversation
                )
        print(len(response.choices))
        return response.choices[0].message.content

def main():
    client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENROUTER_API_KEY"),
            )

    agent = Agent(client, get_user_message)
    agent.run()

if __name__ == "__main__":
    main()

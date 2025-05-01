from openai import OpenAI
from ansi_codes import *
import os
import requests

def get_user_message():
    return input()

def get_weather(latitude, longitude):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m")
    data = response.json()
    return data['current']['temperature_2m']

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

            # message = self.run_inference(conversation)
            message = self.run_tool(conversation)
            conversation.append({
                "role": "assistant",
                "content": message
                })

            print(ANSI_ORANGE + "Model" + ANSI_END + ": ", end="")
            print(message)

    def run_inference(self, conversation):
        response =  self.client.chat.completions.create(
                model=self.model,
                messages=conversation,
                timeout=90,
                temperature=0.0,
                )
        content = response.choices[0].message.content
        if not content:
            return "Error getting response."
        if "<think>" in content:
            if not content:
                return "Error getting response."
            parts = content.split("</think>\n\n")
            think = parts[0][8:-1]
            content = parts[1]
        return content

    def run_tool(self, conversation):
        tools = [{
            "type": "function",
            "name": "get_weather",
            "description": "Get current temperature for a given location.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "City and country e.g. Bogotá, Colombia"
                        }
                    },
                "required": [
                    "location"
                    ],
                "additionalProperties": False
                }
            }]
        response =  self.client.chat.completions.create(
                model=self.model,
                messages=conversation,
                timeout=90,
                temperature=0.0,
                tools=tools
                )

        if not response:
            return "Response not received"

        print(response.__init__)



def main():
    client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENROUTER_API_KEY"),
            )

    agent = Agent(client, get_user_message)
    agent.run()

if __name__ == "__main__":
    main()

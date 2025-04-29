from openai import OpenAI
import os

prompt = "how to build a code editing agent"
code = """"""
message = prompt + "Here is the code:\n```" + code + "```" if code else prompt

client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY"),
        )

completion = client.chat.completions.create(
        extra_headers={
            "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
            "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
            },
        model="tngtech/deepseek-r1t-chimera:free",
        messages=[
            {
                "role": "user",
                "content": message
                }
            ]
        )

print(completion.choices[0].message.content)

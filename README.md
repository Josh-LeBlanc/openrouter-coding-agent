# NOTICE
not working on this any more, too rate limited. trying with ollama instead, then may come back :)
# openrouter-coding-agent
coding agent that uses openrouter because I am a brokie that needs free LLM APIs.

blog that I'm following is in go using anthropic api, we're gonna port it.
# EDIT: using ollama
i was naive and thought openrouter had a high enough rate limit on their APIs to support an agent. they do not. it is 50 requests per day.

so, this will now also support ollama. qwen3 came out yesterday so we're gonna use that 8b model. one different thing about it is that it is a reasoner so we have a think tag to play with as well.
# todo:
implementing tool calls:
[openai docs](https://platform.openai.com/docs/guides/function-calling?api-mode=responses#handling-function-calls)
perplexity says you can use the tool calls with `client.chat.completions.create`, and if there are tool calls they will be in
- __AYO: use the ollama python package instead of openai__
`response.choices[0].message.tool_calls` so check if that is not an empty array then handle the function call
## resources
[thorsten ball blog](https://ampcode.com/how-to-build-an-agent)

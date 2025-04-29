# openrouter-coding-agent
coding agent that uses openrouter because I am a brokie that needs free LLM APIs.

blog that I'm following is in go using anthropic api, we're gonna port it.
# EDIT: using ollama
i was naive and thought openrouter had a high enough rate limit on their APIs to support an agent. they do not. it is 50 requests per day.

so, this will now also support ollama. qwen3 came out yesterday so we're gonna use that 8b model. one different thing about it is that it is a reasoner so we have a think tag to play with as well.
## resources
[thorsten ball blog](https://ampcode.com/how-to-build-an-agent)

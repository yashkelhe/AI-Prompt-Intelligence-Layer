import tiktoken
def estimate_tokens(prompt: str):
    return int(len(prompt.split()) * 1.3)
import tiktoken

def count_tokens(text, model="gpt-4"):
    enc = tiktoken.encoding_for_model(model)
    return len(enc.encode(text))

prompt = "Explain quantum computing in simple terms"
tokens = count_tokens(prompt)
print(f"This prompt costs {tokens} tokens")
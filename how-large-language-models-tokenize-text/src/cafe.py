import tiktoken
enc = tiktoken.get_encoding("cl100k_base")

text = "café"
tokens = enc.encode(text)  # 2 tokens
print([enc.decode([t]) for t in tokens])

import tiktoken
enc = tiktoken.get_encoding("cl100k_base")  # GPT-4 tokenizer

text = "strawberry"
tokens = enc.encode(text)
print([enc.decode([t]) for t in tokens])
# Output: [496, 675, 15717]  (tokens: "str", "aw", "berry")

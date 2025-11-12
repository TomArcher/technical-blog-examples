import tiktoken
enc = tiktoken.get_encoding("cl100k_base")

# Common words token count
text = "the"
tokens = enc.encode(text)  # 1 token
print([enc.decode([t]) for t in tokens])

text = "said"
tokens = enc.encode(text)  # 1 token
print([enc.decode([t]) for t in tokens])

# Rare word token count
text = "antidisestablishmentarianism"
tokens = enc.encode(text)  # 6 tokens
print([enc.decode([t]) for t in tokens])

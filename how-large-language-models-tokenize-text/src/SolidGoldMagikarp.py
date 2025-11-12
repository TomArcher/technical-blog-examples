import tiktoken

# In GPT-3's tokenizer (not cl100k_base):
# enc.encode("SolidGoldMagikarp")
# Output: [46277]  (single token in GPT-3)

# But in GPT-4's tokenizer:
enc = tiktoken.get_encoding("cl100k_base")

tokens = enc.encode("SolidGoldMagikarp")
print([enc.decode([t]) for t in tokens])
# Output: ['Solid', 'Gold', 'Mag', 'ik', 'arp']
import tiktoken
enc = tiktoken.get_encoding("cl100k_base")  # GPT-4 tokenizer

text = "I love 编程"  # "programming" in Chinese
tokens = enc.encode(text)
print([enc.decode([t]) for t in tokens])
# Output: ['I', ' love', ' ', '编', '程']

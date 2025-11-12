import tiktoken
enc = tiktoken.get_encoding("cl100k_base")  # GPT-4 tokenizer

text = "I love supercalifragilisticexpialidocious"
tokens = enc.encode(text)
print([enc.decode([t]) for t in tokens])
# Output: ['I', ' love', ' super', 'cal', 'if', 'rag', 'il', 
# 'istic', 'exp', 'ial', 'id', 'ocious']

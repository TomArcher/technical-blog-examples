import tiktoken
enc = tiktoken.get_encoding("cl100k_base")  # GPT-4 tokenizer

text = "def hello_world():\n    print('Hello!')"
tokens = enc.encode(text)
print([enc.decode([t]) for t in tokens])
# Output: ['def', ' hello', '_world', '():', '\n', '    ', 
# 'print', "('", 'Hello', "!'", ')']

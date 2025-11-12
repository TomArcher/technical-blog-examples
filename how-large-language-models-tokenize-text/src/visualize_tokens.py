import tiktoken

def visualize_tokens(text):
    enc = tiktoken.get_encoding("cl100k_base")
    tokens = enc.encode(text)
    
    print(f"Text: {text}")
    print(f"Tokens: {len(tokens)}\n")
    
    for i, token in enumerate(tokens):
        decoded = enc.decode([token])
        print(f"Token {i}: '{decoded}' (ID: {token})")

# Examples
visualize_tokens("I love programming")
print("\n" + "="*50 + "\n")
visualize_tokens("The quick brown fox jumps over the lazy dog")
print("\n" + "="*50 + "\n")
visualize_tokens(
    "def factorial(n):\n    "
    "return 1 if n == 0 else n * factorial(n-1)"
)
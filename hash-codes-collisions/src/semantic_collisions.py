"""
Semantic collision demonstration: Why meaningful collisions are nearly impossible
Shows that random bytes almost never form valid structured data.
"""

import random
import string
import json
import warnings

def generate_random_bytes(length):
    """Generate random bytes that might hash to a target value."""
    return ''.join(random.choices(string.printable, k=length))

print("=" * 60)
print("SEMANTIC COLLISION TEST: Random Bytes vs Valid Data")
print("=" * 60)

print("\nGenerating 1 million random 100-byte strings...")
print("Testing how many form valid structured data...\n")

# Generate 1 million random attempts
attempts = [generate_random_bytes(100) for _ in range(1_000_000)]

# How many are valid JSON?
valid_json_count = 0
for attempt in attempts:
    try:
        json.loads(attempt)
        valid_json_count += 1
    except:
        pass

print(f"Valid JSON found: {valid_json_count:,}/1,000,000")

# How many are valid Python code?
valid_python_count = 0

# Suppress SyntaxWarnings since we expect invalid code
with warnings.catch_warnings():
    warnings.simplefilter("ignore", SyntaxWarning)

    for attempt in attempts:
        try:
            compile(attempt, '<string>', 'exec')
            valid_python_count += 1
        except:
            pass

print(f"Valid Python found: {valid_python_count:,}/1,000,000")

# Show a few random attempts to demonstrate the gibberish
print("\nSample random strings generated:")
print("-" * 40)
for i in range(3):
    sample = generate_random_bytes(50)
    # Use repr() to safely display the string with escape sequences visible
    print(f"Sample {i+1}: {repr(sample)[:50]}...")

print("\n" + "=" * 60)
print("KEY INSIGHT:")
print("Random data doesn't accidentally become meaningful.")
print("This is why semantic hash collisions are nearly impossible.")
print("=" * 60)
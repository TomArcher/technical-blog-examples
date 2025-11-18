import random
import string
import json

def generate_random_bytes(length):
    """Generate random bytes that might hash to a target value."""
    return ''.join(random.choices(string.printable, k=length))

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

print(f"Valid JSON found: {valid_json_count}/1,000,000")
# Output: Valid JSON found: 0/1,000,000

# How many are valid Python code?
valid_python_count = 0
meaningful_python_count = 0

for attempt in attempts:
    try:
        compile(attempt, '<string>', 'exec')
        valid_python_count += 1
        # Check if it contains meaningful constructs
        if any(keyword in attempt for keyword in
               ['def ', 'class ', 'import ', 'for ', 'if ', 'while ']):
            meaningful_python_count += 1
    except:
        pass

print(f"Valid Python found: {valid_python_count}/1,000,000")
# Output: Valid Python found: ~6,000/1,000,000 (0.6%)

print(f"Meaningful Python found: {meaningful_python_count}/1,000,000")
# Output: Meaningful Python found: 0/1,000,000

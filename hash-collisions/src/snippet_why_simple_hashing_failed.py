import hashlib

# Demonstrating why unsalted hashes are vulnerable
common_passwords = ["password", "123456", "password123", "admin"]
rainbow_table = {}

# Attacker precomputes common password hashes
for pwd in common_passwords:
    rainbow_table[hashlib.sha256(pwd.encode()).hexdigest()] = pwd

# Now they can instantly reverse any matching hash
target_hash = hashlib.sha256("password".encode()).hexdigest()
if target_hash in rainbow_table:
    print(f"Password found: {rainbow_table[target_hash]}")
    # Output: Password found: password
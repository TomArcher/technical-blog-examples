import hashlib

# Modern, secure hash functions
password = "user_password"
sha256_hash = hashlib.sha256(password.encode()).hexdigest()
sha3_hash = hashlib.sha3_256(password.encode()).hexdigest()

print(f"SHA-256 (SECURE): {sha256_hash}")
print(f"SHA-3 (SECURE): {sha3_hash}")

# Also consider BLAKE2 for performance
import hashlib
blake2_hash = hashlib.blake2b(password.encode()).hexdigest()
print(f"BLAKE2b (SECURE & FAST): {blake2_hash}")
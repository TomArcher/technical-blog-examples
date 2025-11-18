import time
import hashlib
import argon2

password = "test_password"

# Time SHA-256 (fast - bad for passwords)
start = time.time()
for _ in range(10000):
    hashlib.sha256(password.encode()).hexdigest()
sha_time = time.time() - start

# Time Argon2 (slow by design - good for passwords)
hasher = argon2.PasswordHasher()
start = time.time()
for _ in range(10):  # Only 10 iterations!
    hasher.hash(password)
argon_time = time.time() - start

print(f"SHA-256 (10,000 hashes): {sha_time:.2f} seconds")
print(f"Argon2 (10 hashes): {argon_time:.2f} seconds")
# SHA-256 is ~10,000x faster - that's the point!
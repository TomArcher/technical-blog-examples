import hashlib

# Also deprecated for security use
password = "user_password"
sha1_hash = hashlib.sha1(password.encode()).hexdigest()
print(f"SHA-1 (DEPRECATED): {sha1_hash}")

# SHAttered attack stats:
# - 9,223,372,036,854,775,808 SHA-1 computations
# - 6,500 CPU years (or 110 GPU years)
# - ~$45,000 in cloud computing costs (2020)
# Modern GPUs: ~15 billion SHA-1 hashes/second
import os
password = 'user_password'

# bcrypt - Battle-tested, widely supported
import bcrypt
bcrypt_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt(rounds=12))
print(f"bcrypt (60 chars):  {bcrypt_hash.decode()}")
# Output: $2b$12$Qw5xgFn8RO7yK3H9Lz5Pzu0GlGXoJe7bVkT9XwRnL3kI8yB5x2G7m

# scrypt - Memory-hard, used by some cryptocurrencies
import hashlib
salt = os.urandom(16)
scrypt_hash = hashlib.scrypt(
    password.encode(),
    salt=salt,
    n=16384, r=8, p=1
)
print(f"scrypt (64 bytes):  {scrypt_hash.hex()[:60]}...")
# Output: a7c3f2e8b9d4a1c6e9f3b8d2c7a4e9f1b3d8c2a7e4f9b1c3d8a2e7f4b9c1...

# PBKDF2 - NIST approved, works everywhere
salt = os.urandom(16)
pbkdf2_hash = hashlib.pbkdf2_hmac(
    'sha256',
    password.encode(),
    salt=salt,
    iterations=100000
)
print(f"PBKDF2 (32 bytes):  {pbkdf2_hash.hex()[:60]}...")
# Output: 5f4dcc3b5aa765d61d8327deb882cf99e8f3a1b2c4d5e6f7a8b9c0d1e2f3a4b5...

# Note the different output formats:
# - bcrypt: includes algorithm, cost, salt, and hash in one string
# - scrypt/PBKDF2: raw bytes, need separate salt storage

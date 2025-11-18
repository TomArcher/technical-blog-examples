# Don't do this anymore!
import hashlib

password = "user_password"
md5_hash = hashlib.md5(password.encode()).hexdigest()
print(f"MD5 (INSECURE): {md5_hash}")

# Collisions can be generated in seconds
# Real attack: 2008 rogue CA certificate using MD5 collisions
# Modern GPUs: ~25 billion MD5 hashes/second
# Status: NEVER use for anything security-critical
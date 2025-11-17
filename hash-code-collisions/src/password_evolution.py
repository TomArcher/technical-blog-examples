"""
Password hashing evolution: 2005 vs 2025
Demonstrates why simple salting is no longer sufficient.
"""

import hashlib
import os
import time

print("=" * 60)
print("PASSWORD HASHING: THEN vs NOW")
print("=" * 60)

# Common password for testing
password = "user_password"

# ========================================
# 2005: SHA-1 + Salt (DON'T DO THIS!)
# ========================================
print("\n2005 Approach: SHA-1 + Salt")
print("-" * 30)

salt = os.urandom(16)
old_hash = hashlib.sha1(password.encode() + salt).hexdigest()

print(f"Password: {password}")
print(f"Salt: {salt.hex()[:32]}...")  # Show first 32 chars
print(f"SHA-1 Hash: {old_hash}")

# Demonstrate the speed problem
start = time.time()
for _ in range(100000):
    hashlib.sha1(password.encode() + salt).hexdigest()
sha1_time = time.time() - start

print(f"\n⚠️  Speed: 100,000 hashes in {sha1_time:.2f} seconds")
print(f"   ({int(100000/sha1_time):,} hashes/second)")
print("\n❌ Problems:")
print("   - SHA-1 is cryptographically broken")
print("   - Too fast (enables brute force attacks)")
print("   - No memory cost (perfect for GPU attacks)")

# ========================================
# 2025: Argon2 (RECOMMENDED)
# ========================================
print("\n2025 Approach: Argon2id")
print("-" * 30)

# pip install argon2-cffi
from argon2 import PasswordHasher

hasher = PasswordHasher(
    memory_cost=65536,  # 64 MB of memory required
    time_cost=3,        # Number of iterations
    parallelism=4,      # Parallel threads
)

password_hash = hasher.hash(password)

print(f"Password: {password}")
print(f"Argon2 Hash: {password_hash[:60]}...")

# Demonstrate the deliberate slowness
start = time.time()
for _ in range(10):  # Only 10 iterations!
    hasher.hash(password)
argon2_time = time.time() - start

print(f"\n✅ Speed: 10 hashes in {argon2_time:.2f} seconds")
print(f"   ({int(10/argon2_time):.1f} hashes/second)")

print("\n✅ Benefits:")
print("   - Memory-hard (64MB per attempt)")
print("   - Time-expensive by design")
print("   - Resistant to GPU/ASIC attacks")
print("   - Built-in salt generation")
print("   - Version tracking for future upgrades")

# ========================================
# The Speed Difference
# ========================================
print("\n" + "=" * 60)
print("THE KEY INSIGHT:")
print(f"SHA-1 is {int((100000/sha1_time)/(10/argon2_time)):,}x faster than Argon2")
print("For passwords, slower is better - it prevents brute force!")
print("=" * 60)

# Verify the password works
try:
    hasher.verify(password_hash, password)
    print("\n✅ Password verification successful")
except:
    print("\n❌ Password verification failed")
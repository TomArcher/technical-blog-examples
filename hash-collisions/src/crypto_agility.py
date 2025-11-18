"""
Crypto-agility demonstration: Future-proofing hash functions
Shows how to design systems that can migrate to new algorithms
without breaking existing data.
"""

import hashlib
import json
from enum import Enum


class HashVersion(Enum):
    SHA256_V1 = "sha256_v1"
    SHA3_256_V2 = "sha3_256_v2"
    BLAKE3_V3 = "blake3_v3"


class VersionedHasher:
    def __init__(self):
        self.current_version = HashVersion.SHA3_256_V2

    def hash_with_version(self, data):
        """Store algorithm version with hash."""
        if self.current_version == HashVersion.SHA256_V1:
            hash_value = hashlib.sha256(data.encode()).hexdigest()
        elif self.current_version == HashVersion.SHA3_256_V2:
            hash_value = hashlib.sha3_256(data.encode()).hexdigest()

        return {
            "version": self.current_version.value,
            "hash": hash_value
        }

    def verify(self, data, versioned_hash):
        """Verify using the original algorithm."""
        version = HashVersion(versioned_hash["version"])

        if version == HashVersion.SHA256_V1:
            computed = hashlib.sha256(data.encode()).hexdigest()
        elif version == HashVersion.SHA3_256_V2:
            computed = hashlib.sha3_256(data.encode()).hexdigest()

        return computed == versioned_hash["hash"]


# Demonstration
print("=" * 60)
print("CRYPTO-AGILITY: Preparing for Algorithm Migration")
print("=" * 60)

hasher = VersionedHasher()

# Start with SHA3-256 (current default)
print("\n1. Hashing with current algorithm (SHA3-256):")
data = "important data"
stored_hash = hasher.hash_with_version(data)
print(json.dumps(stored_hash, indent=2))

# Verify it works
is_valid = hasher.verify(data, stored_hash)
print(f"   Verification: {'✅ Valid' if is_valid else '❌ Invalid'}")

# Simulate algorithm upgrade
print("\n2. System upgrade to SHA-256 (for demonstration):")
hasher.current_version = HashVersion.SHA256_V1
new_data = "new important data"
new_hash = hasher.hash_with_version(new_data)
print(json.dumps(new_hash, indent=2))

# Old data still verifies with old algorithm
print("\n3. Verifying old data with its original algorithm:")
is_valid = hasher.verify(data, stored_hash)
print(f"   Old data (SHA3-256): {'✅ Valid' if is_valid else '❌ Invalid'}")

# New data verifies with new algorithm
is_valid = hasher.verify(new_data, new_hash)
print(f"   New data (SHA-256): {'✅ Valid' if is_valid else '❌ Invalid'}")

print("\n" + "=" * 60)
print("KEY INSIGHTS:")
print("• Store the algorithm version with every hash")
print("• Old data remains verifiable with original algorithm")
print("• System can evolve without breaking existing hashes")
print("• Essential for systems that must last 20+ years")
print("=" * 60)
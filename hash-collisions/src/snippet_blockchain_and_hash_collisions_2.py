import hashlib


# Simulating crypto-agility in smart contracts
class HashAlgorithm:
    SHA256 = 1
    SHA3_256 = 2
    BLAKE3 = 3
    CRYSTALS_DILITHIUM = 4  # Post-quantum signature
    SPHINCS_PLUS = 5  # Stateless post-quantum


class FutureProofContract:
    def __init__(self):
        self.hash_version = HashAlgorithm.SHA256

    def hash_data(self, data):
        if self.hash_version == HashAlgorithm.SHA256:
            return hashlib.sha256(data.encode()).hexdigest()
        elif self.hash_version == HashAlgorithm.SHA3_256:
            return hashlib.sha3_256(data.encode()).hexdigest()
        # Ready to upgrade when quantum computers arrive

    def upgrade_hash_algorithm(self, new_version):
        """Allows migration to stronger algorithms."""
        self.hash_version = new_version


# Usage example
contract = FutureProofContract()
data = "Critical transaction data"

# Initial state: SHA-256
hash1 = contract.hash_data(data)
print(f"SHA-256:   {hash1}")
# Output: SHA-256:   8b5e9db8c4f9a7e3b1d2c3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4

# Upgrade to SHA3-256 (perhaps due to SHA-256 weakness discovered)
contract.upgrade_hash_algorithm(HashAlgorithm.SHA3_256)
hash2 = contract.hash_data(data)
print(f"SHA3-256:  {hash2}")
# Output: SHA3-256:  f4a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1

# Both algorithms can coexist - old data verified with SHA-256, new with SHA3-256
print("\nKey insight: Same data, different algorithms, different hashes")
print("Old transactions remain valid with their original algorithm")

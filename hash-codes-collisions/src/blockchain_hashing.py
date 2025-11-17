#!/usr/bin/env python3
"""
blockchain_hashing.py

Demonstrates how blockchain systems like Bitcoin use hashing for security,
including double SHA-256, proof-of-work concepts, and crypto-agility patterns
for future-proofing against quantum threats.
"""

import hashlib
import time
import json
from enum import Enum
from typing import Dict, Any


def bitcoin_double_sha256():
    """
    Demonstrates Bitcoin's paranoid approach: double SHA-256 hashing.
    """
    print("=" * 60)
    print("Bitcoin's Double SHA-256 Approach")
    print("=" * 60)

    def bitcoin_hash(data: str) -> str:
        """Bitcoin uses double SHA-256 for extra security."""
        # First round of SHA-256
        first_hash = hashlib.sha256(data.encode()).digest()
        # Second round of SHA-256 on the first hash
        second_hash = hashlib.sha256(first_hash).digest()
        return second_hash.hex()

    # Example block header components
    block_header = "version:4|prev_block:000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f|merkle_root:4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b|timestamp:1231006505|bits:486604799|nonce:2083236893"

    # Single SHA-256 (what most systems use)
    single_hash = hashlib.sha256(block_header.encode()).hexdigest()

    # Double SHA-256 (what Bitcoin uses)
    double_hash = bitcoin_hash(block_header)

    print("Block header data (simplified):")
    print(f"  {block_header[:80]}...")
    print()
    print("Single SHA-256:")
    print(f"  {single_hash}")
    print()
    print("Double SHA-256 (Bitcoin's choice):")
    print(f"  {double_hash}")
    print()
    print("Why double hashing?")
    print("  • Protection against length-extension attacks")
    print("  • Extra security margin against future attacks")
    print("  • Computational cost is negligible")
    print()


def mining_simulation():
    """
    Simulates the mining process - finding a hash with leading zeros.
    """
    print("=" * 60)
    print("Proof-of-Work Mining Simulation")
    print("=" * 60)

    def mine_block(data: str, difficulty: int) -> tuple:
        """
        Find a nonce that produces a hash with 'difficulty' leading zeros.
        """
        nonce = 0
        start_time = time.time()
        target = "0" * difficulty

        while True:
            block_data = f"{data}|nonce:{nonce}"
            hash_result = hashlib.sha256(block_data.encode()).hexdigest()

            if hash_result.startswith(target):
                elapsed = time.time() - start_time
                return nonce, hash_result, elapsed

            nonce += 1

            # Stop after reasonable attempts for demo
            if nonce > 1000000:
                return None, None, time.time() - start_time

    # Mine with increasing difficulty
    block_data = "transactions:Alice->Bob:10BTC|Bob->Charlie:5BTC"

    for difficulty in [1, 2, 3, 4]:
        print(f"Mining with difficulty {difficulty} (need {difficulty} leading zeros)...")
        nonce, hash_result, elapsed = mine_block(block_data, difficulty)

        if nonce is not None:
            print(f"  ✅ Found valid hash after {nonce:,} attempts in {elapsed:.3f} seconds")
            print(f"  Hash: {hash_result}")
        else:
            print(f"  ❌ Gave up after 1,000,000 attempts ({elapsed:.3f} seconds)")
        print()

    print("Notice how difficulty increases exponentially:")
    print("  • Each additional zero makes mining ~16x harder")
    print("  • Bitcoin adjusts difficulty to maintain ~10 minute blocks")
    print()


def merkle_tree_demo():
    """
    Demonstrates how blockchain uses Merkle trees for efficient verification.
    """
    print("=" * 60)
    print("Merkle Tree for Transaction Verification")
    print("=" * 60)

    def hash_pair(left: str, right: str) -> str:
        """Hash two values together."""
        combined = left + right
        return hashlib.sha256(combined.encode()).hexdigest()

    # Simulate transactions
    transactions = [
        "Alice->Bob:10",
        "Bob->Charlie:5",
        "Charlie->David:3",
        "David->Eve:2"
    ]

    # Hash individual transactions (leaf nodes)
    tx_hashes = [hashlib.sha256(tx.encode()).hexdigest() for tx in transactions]

    print("Individual transaction hashes:")
    for tx, tx_hash in zip(transactions, tx_hashes):
        print(f"  {tx:20} → {tx_hash[:16]}...")
    print()

    # Build Merkle tree
    level = tx_hashes
    tree_levels = [level]

    while len(level) > 1:
        next_level = []
        for i in range(0, len(level), 2):
            if i + 1 < len(level):
                parent = hash_pair(level[i], level[i + 1])
            else:
                # Odd number of nodes, duplicate the last one
                parent = hash_pair(level[i], level[i])
            next_level.append(parent)
        level = next_level
        tree_levels.append(level)

    merkle_root = level[0] if level else None

    print(f"Merkle root: {merkle_root[:32]}...")
    print()
    print("Benefits of Merkle trees in blockchain:")
    print("  • Efficient proof of transaction inclusion")
    print("  • Can verify specific transaction without full block")
    print("  • Compact representation of all transactions")
    print()


def crypto_agility_demo():
    """
    Demonstrates how future-proof systems can migrate hash algorithms.
    """
    print("=" * 60)
    print("Crypto-Agility: Preparing for Post-Quantum Future")
    print("=" * 60)

    class HashAlgorithm(Enum):
        SHA256 = "sha256_v1"
        SHA3_256 = "sha3_256_v2"
        BLAKE3 = "blake3_v3"
        FUTURE_QUANTUM_RESISTANT = "post_quantum_v4"

    class FutureProofBlockchain:
        def __init__(self):
            self.current_version = HashAlgorithm.SHA256
            self.blocks = []

        def hash_data(self, data: str) -> Dict[str, str]:
            """Hash data with version tracking."""
            if self.current_version == HashAlgorithm.SHA256:
                hash_value = hashlib.sha256(data.encode()).hexdigest()
            elif self.current_version == HashAlgorithm.SHA3_256:
                hash_value = hashlib.sha3_256(data.encode()).hexdigest()
            elif self.current_version == HashAlgorithm.BLAKE3:
                # Simplified - would use actual blake3 library
                hash_value = hashlib.sha256(f"blake3:{data}".encode()).hexdigest()
            else:
                # Placeholder for future quantum-resistant algorithm
                hash_value = hashlib.sha256(f"quantum:{data}".encode()).hexdigest()

            return {
                "algorithm": self.current_version.value,
                "hash": hash_value,
                "timestamp": int(time.time())
            }

        def add_block(self, data: str):
            """Add a block with current hash algorithm."""
            block = {
                "data": data,
                "hash_info": self.hash_data(data)
            }
            self.blocks.append(block)
            return block

        def upgrade_algorithm(self, new_algorithm: HashAlgorithm):
            """Upgrade to a new hash algorithm."""
            old_algo = self.current_version.value
            self.current_version = new_algorithm
            print(f"  🔄 Upgraded from {old_algo} to {new_algorithm.value}")

        def verify_block(self, block: Dict[str, Any]) -> bool:
            """Verify a block using its original algorithm."""
            algo = block["hash_info"]["algorithm"]
            data = block["data"]

            # Re-compute hash with original algorithm
            if algo == HashAlgorithm.SHA256.value:
                computed = hashlib.sha256(data.encode()).hexdigest()
            elif algo == HashAlgorithm.SHA3_256.value:
                computed = hashlib.sha3_256(data.encode()).hexdigest()
            else:
                # Handle other algorithms
                computed = hashlib.sha256(f"blake3:{data}".encode()).hexdigest()

            return computed == block["hash_info"]["hash"]

    # Simulate blockchain evolution
    blockchain = FutureProofBlockchain()

    print("Simulating blockchain evolution over time:")
    print()

    # Era 1: SHA-256
    print("Era 1: Using SHA-256 (current Bitcoin/early Ethereum)")
    blockchain.add_block("Genesis block")
    blockchain.add_block("Transaction batch #1")

    # Era 2: Upgrade to SHA3
    print("\nEra 2: Quantum computers emerging...")
    blockchain.upgrade_algorithm(HashAlgorithm.SHA3_256)
    blockchain.add_block("Transaction batch #2")

    # Era 3: Move to BLAKE3
    print("\nEra 3: Need faster hashing...")
    blockchain.upgrade_algorithm(HashAlgorithm.BLAKE3)
    blockchain.add_block("Transaction batch #3")

    # Verify all blocks still work
    print("\nVerifying all blocks with their original algorithms:")
    for i, block in enumerate(blockchain.blocks):
        is_valid = blockchain.verify_block(block)
        algo = block["hash_info"]["algorithm"]
        status = "✅" if is_valid else "❌"
        print(f"  Block {i}: {algo:20} {status}")

    print()
    print("Key insights:")
    print("  • Store algorithm version with each hash")
    print("  • Old blocks remain valid with original algorithm")
    print("  • System can evolve without breaking history")
    print("  • Essential for 30+ year blockchain survival")
    print()


def collision_implications():
    """
    Explains what happens if SHA-256 actually breaks.
    """
    print("=" * 60)
    print("If SHA-256 Falls: Blockchain Implications")
    print("=" * 60)

    print("Current blockchain dependency on SHA-256:")
    print("  • Bitcoin: ~$1.5 trillion market cap")
    print("  • Ethereum: ~$400 billion market cap")
    print("  • Thousands of other cryptocurrencies")
    print()

    print("What breaks if SHA-256 has practical collisions:")
    print()
    print("1. Double-spend attacks become possible")
    print("   → Create two valid blocks with same hash")
    print("   → Network can't determine canonical chain")
    print()
    print("2. History becomes mutable")
    print("   → Generate alternate valid histories")
    print("   → Proof-of-work becomes meaningless")
    print()
    print("3. Digital signatures compromised")
    print("   → Forge transactions")
    print("   → Steal from any address")
    print()
    print("4. Mining becomes trivial")
    print("   → Anyone can generate valid blocks instantly")
    print("   → Consensus mechanism fails")
    print()
    print("Emergency response plans:")
    print("  • Hard fork to new algorithm (requires consensus)")
    print("  • Freeze blockchain until upgrade")
    print("  • Migrate to quantum-resistant algorithms")
    print("  • Some value will inevitably be lost in transition")
    print()


def main():
    """Run all blockchain hashing demonstrations."""
    print("\n⛓️ BLOCKCHAIN HASHING: BILLIONS DEPEND ON COLLISION RESISTANCE\n")

    bitcoin_double_sha256()
    mining_simulation()
    merkle_tree_demo()
    crypto_agility_demo()
    collision_implications()

    print("=" * 60)
    print("Key Takeaway: Blockchain security = hash function security")
    print("=" * 60)


if __name__ == "__main__":
    main()
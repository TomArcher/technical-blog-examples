import hashlib

def bitcoin_hash(data):
    """Bitcoin uses double SHA-256 for extra security."""
    first_hash = hashlib.sha256(data.encode()).digest()
    second_hash = hashlib.sha256(first_hash).digest()
    return second_hash.hex()

# Example Bitcoin block header hashing
block_header = "version|prev_block|merkle_root|timestamp|bits|nonce"
block_hash = bitcoin_hash(block_header)
print(f"Bitcoin block hash: {block_hash}")
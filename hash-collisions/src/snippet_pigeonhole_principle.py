import hashlib

# These vastly different inputs...
short_text = "Hi"
medium_text = "A" * 1000  # 1KB
long_text = "B" * 1_000_000  # 1MB

# ...all produce the same length output
print(len(hashlib.sha256(short_text.encode()).digest()))   # 32 bytes
print(len(hashlib.sha256(medium_text.encode()).digest()))  # 32 bytes
print(len(hashlib.sha256(long_text.encode()).digest()))    # 32 bytes
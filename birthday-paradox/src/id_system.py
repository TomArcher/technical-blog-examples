# id_system.py

from enum import Enum

class IDSystem(Enum):
    """Common ID systems and their bit spaces"""
    INT32 = 32  # Traditional auto-increment
    INT64 = 64  # Modern databases
    UUID_V4 = 122  # Random UUID (122 random bits)
    SHA256 = 256  # Cryptographic hashes

    @property
    def space_size(self) -> int:
        return 2 ** self.value

    @property
    def description(self) -> str:
        return {
            self.INT32: "32-bit integer",
            self.INT64: "64-bit integer",
            self.UUID_V4: "UUID version 4",
            self.SHA256: "SHA-256 hash"
        }[self]
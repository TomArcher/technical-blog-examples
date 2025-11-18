import hashlib
import os

# Old way (DON'T DO THIS)
password = "user_password"
salt = os.urandom(16)
old_hash = hashlib.sha1(
    password.encode() + salt
).hexdigest()

# Seemed secure at the time!
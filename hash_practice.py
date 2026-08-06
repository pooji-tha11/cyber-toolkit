import hashlib

text = "Hello"
md5_hash = hashlib.md5(text.encode()).hexdigest()
sha1_hash = hashlib.sha1(text.encode()).hexdigest()
sha256_hash = hashlib.sha256(text.encode()).hexdigest()

print(f"Text: {text}")
print(f"MD5:    {md5_hash}")
print(f"SHA-1:  {sha1_hash}")
print(f"SHA-256: {sha256_hash}")


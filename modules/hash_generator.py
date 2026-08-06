import hashlib

def generate_hashes(text):
    encoded_text = text.encode()

    return {
        "md5": hashlib.md5(encoded_text).hexdigest(),
        "sha1": hashlib.sha1(encoded_text).hexdigest(),
        "sha256": hashlib.sha256(encoded_text).hexdigest()
    }

def generate_file_hashes(file_bytes):
    return {
        "md5": hashlib.md5(file_bytes).hexdigest(),
        "sha1": hashlib.sha1(file_bytes).hexdigest(),
        "sha256": hashlib.sha256(file_bytes).hexdigest()
    }
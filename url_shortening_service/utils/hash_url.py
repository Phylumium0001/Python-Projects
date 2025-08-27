# Hash Url
from hashlib import sha256
from os import urandom


def generate_hash_value(normalized_url: str):
    url_byte = bytes(normalized_url, encoding="utf-8")
    hash = sha256(url_byte)
    return hash.hexdigest()


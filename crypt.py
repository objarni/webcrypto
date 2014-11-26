import base64


def rolling_xor(string, crypto):
    crypto = (crypto*100)[:len(string)]
    assert len(string) == len(crypto)
    assert type(string) == str
    assert type(crypto) == str
    return b''.join(chr(ord(a) ^ ord(b)) for (a, b) in zip(string, crypto))


def encrypt(cleartext, crypto):
    bytes = rolling_xor(cleartext, crypto)
    return base64.b64encode(bytes)


def decrypt(encrypted, crypto):
    bytes = base64.b64decode(encrypted)
    return rolling_xor(bytes, crypto)

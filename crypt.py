import base64


def rolling_xor(string, crypto):
    crypto = (crypto*2)[:len(string)]
    assert type(string) == str
    assert type(crypto) == str
    return b''.join(chr(ord(a) ^ ord(b)) for (a, b) in zip(string, crypto))


def encrypt(cleartext, crypto):
    # We want a strong encryption - a crypto comparable in length
    # to the cleartext ensures that no statistical method can
    # decrypt with brute-force.
    # Note: this is only an hypothesis that remains to be proven
    # or disproven by my Facebook friends ;)
    if len(crypto) < len(cleartext) * 0.50:
        raise ValueError('Crypto must be at least 50%% of cleartext length')
    bytes = rolling_xor(cleartext, crypto)
    return base64.b64encode(bytes)


def decrypt(encrypted, crypto):
    bytes = base64.b64decode(encrypted)
    return rolling_xor(bytes, crypto)

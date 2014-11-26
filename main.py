from crypt import encrypt, decrypt
from secret import CLEARTEXT, CRYPTO

if __name__ == '__main__':
    encrypted = encrypt(CLEARTEXT, CRYPTO)
    decrypted = decrypt(encrypted, CRYPTO)
    print 'cleartext ' + CLEARTEXT
    print 'encrypted ' + encrypted
    print 'decrypted ' + decrypted
    assert decrypted == CLEARTEXT

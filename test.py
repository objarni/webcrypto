import unittest
import crypt


class Tests(unittest.TestCase):

    def test_decrypting_encrypted_string_works(self):
        cleartext = 'abc def'
        crypto = 'SecretPassword'
        encrypted = crypt.encrypt(cleartext, crypto)
        decrypted = crypt.decrypt(encrypted, crypto)
        self.assertEqual(cleartext, decrypted)

    def test_encrypted_string_is_different_from_cleartext(self):
        self.assertNotEqual('abc', crypt.encrypt('abc', 'password'))

    def test_too_short_crypto_gives_exception(self):
        try:
            crypt.encrypt('some text', 'a')
            self.fail('Expected exception')
        except ValueError:
            pass


if __name__ == '__main__':
    unittest.main()

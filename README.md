webcrypto
=========

Is it possible to keep a small amount of symmetrically encrypted data public
on the web and still sleep good at night?

This is an experiment attempting to answer that question.


Dependencies
------------
Written in Python 2.7. No other dependencies.


Run
---
Assuming there is a file "secret.py" containing two byte string constants CLEARTEXT and CRYPTO, you can test encrypting and decrypting CLEARTEXT using:

    python main.py

For example, if secret.py contains these two lines:

	CLEARTEXT = b'This is some unencrypted text.'
	CRYPTO = b'My super secret and very long password'

.. then you should get this output:

	$ python main.py
	cleartext This is some unencrypted text.
	encrypted GRFJAFUZFlJTHAgGUhAaRQ8NFlkGERcdABgKFhMO
	decrypted This is some unencrypted text.


Run tests
---------

	python test.py


from secureconfig import SecureConfigParser

# starting with an ini file that has unencrypted entries:
configpath = 'config.ini'

import os

key_env = os.urandom(24)

print os.urandom(24)

scfg = SecureConfigParser.from_env(key_env)
scfg.read(configpath)

username = scfg.get('credentials', 'username')
password = scfg.get('credentials', 'password')

# IMPORTANT: supply encrypt=True to encrypt values.
scfg.set('credentials', 'password', 'better_password', encrypt=True)

fh=open('/path/to/new_scfp.ini', 'w')
scfg.write(fh)
fh.close()


from secureconfig import SecureConfig

config = SecureConfig.from_file('.keys/aes_key', filepath='/path/to/serialized.enc')

cfg = config.cfg

username = cfg['username']
password = cfg['password']

connection = GetSomeConnection(username, password)

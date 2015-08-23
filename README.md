This is mostly a POC for storing public keys in vault.


You should be able to use the current version of this script, the token lookup would need a bit more cleanup.


With the folowing configuration in your sshd you should be able to use it:


AuthorizedKeysCommand /usr/bin/vault_ssh_keys.py
AuthorizedKeysCommandRunAs nobody

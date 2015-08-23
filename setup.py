
from setuptools import setup
setup(name='vault-key',
      version='0.1',
      description='use vault as a backend for ssh keys',
      author='gcmalloc',
      url='http://github.com/gcmalloc/vault-ssh-keys',
      py_modules=['vault_ssh_keys'],
      install_requires=['hvac'],
      scripts=['bin/vault_ssh_keys'])

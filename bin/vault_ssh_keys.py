#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.parse as urlparse
import os
import argparse
import logging

import hvac


class VaultKey():
    def __init__(self, host, port, token, base, ssl=True):
        """Built the url and connect the client to vault
        """
        schema = 'http' if ssl else 'https'
        self.url = "{}://{}:{}/".format(schema, host, port)
        logging.debug("url used to connect to vault will be:" + self.url)
        self.base = base
        self.hvac_client = hvac.Client(self.url, token=token, verify=ssl)

    def read(self, user):
        self.hvac_client.read(os.path.join(self.base, user))

    def write_key(self, user, key):
        self.hvac_client.write(os.path.join(self.base, user), key)


def main(args):
    vault_client = VaultKey(host=args.host, port=args.port,
                            token=args.token, base=args.base,
                            ssl=not args.insecure)
    if args.write:
        vault_client.write(args.user, sys.stdin.read())
    else:
        vault_client.read(args.user)


def get_parser():
    """return the argparse parser for this program"""
    parser = argparse.ArgumentParser(__name__)
    parser.add_argument('-H', '--host', default='localhost',
                        help='host to connect for the vault api')
    parser.add_argument('-P', '--port', default=8200, type=int,
                        help='port to connect for the vault api')
    parser.add_argument('-B', '--base', default='/keys/',
                        help='base url for the keys')
    parser.add_argument('-i', '--insecure', default=False,
                        help='disable tls and certificate verification')
    parser.add_argument('-t', '--token', default='',
                        help='set the token that will be used to authenticate'
                        ' against vault')
    parser.add_argument('-w', '--write', default=False, action='store_true',
                        help='the default is to read a public key, this will'
                        ' overwrite the user public key using stdin')
    parser.add_argument('user')
    return parser


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    logging.debug("arguments are : {!s}".format(args))
    main(args)

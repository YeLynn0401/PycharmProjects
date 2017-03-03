#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# setup logging
import base64
from binascii import hexlify
import getpass
import os
import select
import socket
import sys
import time
import traceback
from paramiko.py3compat import input

import paramiko

try:
    import interactive
except ImportError:
    from demos import interactive


class conn:
    def __init__(self, client_name):
        # paramiko.util.log_to_file('demo.log')

        username = ''
        if len(sys.argv) > 1:
            hostname = sys.argv[1]
            if hostname.find('@') >= 0:
                username, hostname = hostname.split('@')
        else:
            hostname = '192.168.100.5'
        if len(hostname) == 0:
            print('*** Hostname required.')
            sys.exit(1)
        port = 22
        if hostname.find(':') >= 0:
            hostname, portstr = hostname.split(':')
            port = int(portstr)

        # now connect
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((hostname, port))
        except Exception as e:
            print('*** Connect failed: ' + str(e))
            traceback.print_exc()
            sys.exit(1)

        try:
            self.t = paramiko.Transport(sock)
            try:
                self.t.start_client()
            except paramiko.SSHException:
                print('*** SSH negotiation failed.')
                sys.exit(1)

            try:
                keys = paramiko.util.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))
            except IOError:
                try:
                    keys = paramiko.util.load_host_keys(os.path.expanduser('~/ssh/known_hosts'))
                except IOError:
                    print('*** Unable to open host keys file')
                    keys = {}

            # check server's host key -- this is importanself.t.
            key = self.t.get_remote_server_key()
            if hostname not in keys:
                print('*** WARNING: Unknown host key!')
            elif key.get_name() not in keys[hostname]:
                print('*** WARNING: Unknown host key!')
            elif keys[hostname][key.get_name()] != key:
                print('*** WARNING: Host key has changed!!!')
                sys.exit(1)
            else:
                print('*** Host key OK.')

            # get username
            if username == '':
                # default_username = getpass.getuser()
                default_username = 'root'
                username = default_username
                if len(username) == 0:
                    username = default_username

            self.agent_auth(self.t, username)
            if not self.t.is_authenticated():
                self.manual_auth(username, hostname)
            if not self.t.is_authenticated():
                print('*** Authentication failed. :(')
                self.t.close()
                sys.exit(1)

            chan = self.t.open_session()
            chan.get_pty()
            chan.invoke_shell()
            print('*** Here we go!\n')
            interactive.interactive_shell(client_name, hostname, username, chan)
            chan.close()
            self.t.close()

        except Exception as e:
            print('*** Caught exception: ' + str(e.__class__) + ': ' + str(e))
            traceback.print_exc()
            try:
                self.t.close()
            except:
                pass
            sys.exit(1)

    def agent_auth(self, transport, username):
        """
        Attempt to authenticate to the given transport using any of the private
        keys available from an SSH agent.
        """

        agent = paramiko.Agent()
        agent_keys = agent.get_keys()
        if len(agent_keys) == 0:
            return

        for key in agent_keys:
            print('Trying ssh-agent key %s' % hexlify(key.get_fingerprint()))
            try:
                transport.auth_publickey(username, key)
                print('... success!')
                return
            except paramiko.SSHException:
                print('... nope.')

    def manual_auth(self, username, hostname):
        default_auth = 'p'
        auth = ''
        if len(auth) == 0:
            auth = default_auth

        if auth == 'r':
            default_path = os.path.join(os.environ['HOME'], '.ssh', 'id_rsa')
            path = input('RSA key [%s]: ' % default_path)
            if len(path) == 0:
                path = default_path
            try:
                key = paramiko.RSAKey.from_private_key_file(path)
            except paramiko.PasswordRequiredException:
                password = getpass.getpass('RSA key password: ')
                key = paramiko.RSAKey.from_private_key_file(path, password)
            self.t.auth_publickey(username, key)
        elif auth == 'd':
            default_path = os.path.join(os.environ['HOME'], '.ssh', 'id_dsa')
            path = input('DSS key [%s]: ' % default_path)
            if len(path) == 0:
                path = default_path
            try:
                key = paramiko.DSSKey.from_private_key_file(path)
            except paramiko.PasswordRequiredException:
                password = getpass.getpass('DSS key password: ')
                key = paramiko.DSSKey.from_private_key_file(path, password)
            self.t.auth_publickey(username, key)
        else:
            # pw = getpass.getpass('Password for %s@%s: ' % (username, hostname))
            pw = '123456'
            self.t.auth_password(username, pw)
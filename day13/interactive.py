# Copyright (C) 2003-2007  Robey Pointer <robeypointer@gmail.com>
#
# This file is part of paramiko.
#
# Paramiko is free software; you can redistribute it and/or modify it under the
# terms of the GNU Lesser General Public License as published by the Free
# Software Foundation; either version 2.1 of the License, or (at your option)
# any later version.
#
# Paramiko is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Paramiko; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA.


import socket
import sys
import time
from paramiko.py3compat import u

# windows does not have termios...
try:
    import termios
    import tty
    has_termios = True
except ImportError:
    has_termios = False


def interactive_shell(client_name, hostname, username, chan):
    if has_termios:
        posix_shell(client_name, hostname, username, chan)
    else:
        try:
            windows_shell(client_name, hostname, username, chan)
        except:
            pass


def posix_shell(client_name, hostname, username, chan):
    import select
    print('action')
    oldtty = termios.tcgetattr(sys.stdin)
    try:
        tty.setraw(sys.stdin.fileno())
        tty.setcbreak(sys.stdin.fileno())
        chan.settimeout(0.0)
        tem = []
        while True:
            r, w, e = select.select([chan, sys.stdin], [], [])

            if chan in r:
                try:
                    x = u(chan.recv(1024))
                    # print(x)
                    if len(x) == 0:
                        sys.stdout.write('\r\n*** EOF\r\n')
                        break
                    sys.stdout.write(x)

                    sys.stdout.flush()
                    # print(x)
                except socket.timeout:
                    pass
            if sys.stdin in r:

                x = sys.stdin.read(1)
                if len(x) == 0:
                    break
                chan.send(x)
                # print(x.encode())
                if '\r' in x:
                    print('\r\n{}'.format(time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())), client_name, hostname,
                          username, 'cmd:', ''.join(tem))
                    tem = []
                    continue
                    # print('huanhang')
                tem.append(x)

    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, oldtty)
        print('aaa')

    
# thanks to Mike Looijmans for this code
def windows_shell(client_name,hostname, username, chan):
    import threading
    sys.stdout.write("Line-buffered terminal emulation. Press F6 or ^Z to send EOF.\r\n\r\n")

    def writeall(sock):
        while True:
            data = sock.recv(256)
            if not data:
                sys.stdout.write('\r\n*** EOF ***\r\n\r\n')
                sys.stdout.flush()
                break
            sys.stdout.write(data.decode())
            sys.stdout.flush()
    writer = threading.Thread(target=writeall, args=(chan,))
    writer.start()

    try:
        tem = []
        while True:
            d = sys.stdin.read(1)
            if not d:
                break
            chan.send(d)
            if d == '\n':
                cmd_log = ' '.join(('{}'.format(time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())), client_name, hostname, username, 'cmd:', ''.join(tem), '\n'))
                print(cmd_log)

                with open('logs/cmd.log', 'a', encoding='utf8') as f_log:
                    f_log.write(cmd_log)
                tem = []
                continue
            tem.append(d)
    except Exception as e:
        # user hit ^Z or F6
        print(e)

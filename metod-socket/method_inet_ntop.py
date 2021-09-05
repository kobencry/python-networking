#!/usr/bin/env python3.8

import socket

# method inet_ntop() mengubah alamat IP dalam format biner yang dikemas ke format string

# Syntax
# socket.inet_ntop(family, biner)

# Parameter Value
# family socket: socket.AF_INET, biner

ip_biner = b'\xd8\xef&x'
ip_string = socket.inet_ntop(socket.AF_INET, ip_biner)
print(ip_string)


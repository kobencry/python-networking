#!/usr/bin/env python3.8

import socket

# method inet_pton() mengubah alamat IP dalam format string menjadi format biner yang dikemas

# Syntax
# socket.inet_pton(socket.AF_INET, host)

# Parameter Value
# family socket: socket.AF_INET,  host

# mengkonversi IPv4
host = '127.0.0,1'
ip_biner = socket.inet_pton(socket.AF_INET, host)
print(ip_biner)

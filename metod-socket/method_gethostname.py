#!/usr/bin/env python3.8

import socket

# method gethostname() menampilkan nama host dari system saat ini
# dimana interpreter python dieksekusi

# Syntax
# socket.gethostname()

# Parameter Value
# none

host = socket.gethostname()
print(host)

# contoh menggabungkan method socket.gethostbyname(value)
s = socket.gethostbyname(host)
print(s)


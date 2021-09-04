#!/usr/bin/env python3.8
import socket

# method gethostbyname_ex(value) menampilkan type data tuple yang berisi informasi:
# > nama host
# > nama alias dari nama host
# > alamat ip lain dari nama host

# Syntax
# socket.gethostbyname_ex(value)

# Parameter Value
# ip/host

host = "localhost" # 127.0.0.1
s = socket.gethostbyname_ex(host)
print(s)


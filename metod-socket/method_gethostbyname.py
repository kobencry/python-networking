#!/usr/bin/env python3.8
import socket

# method gethostbyname(value) menampilkan alamat ip dari host domain

# Syntax
# socket.gethostbyname(value)

# Parameter Value
# ip/nama domain

host = "localhost" # 127.0.0.1
s = socket.gethostbyname(host)
print(s)


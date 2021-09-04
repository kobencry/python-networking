#!/usr/bin/env python3.8

# method gethostbyaddr(value) menampilkan alamat ip dan nama domain
# dalam bentuk type tuple

# Syntax
# socket.gethostbyaddr(value)

# Paramater value
# ip/nama domain

host = "127.0.0.1" # localhost
s = socket.gethostbyaddr(host)
print(s)

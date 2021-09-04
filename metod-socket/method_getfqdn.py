#!/usr/bin/env/ python3.8
import socket

# method getfqdn() mendapatkan nama domain sepenuhnya berkualitas dari host

# Syntax
# s.getfqdn()

# Parameter Value
# None


host = "localhost" # 127.0.0.1
s = socket.getfqdn(host)
print("nama host domain:", s)


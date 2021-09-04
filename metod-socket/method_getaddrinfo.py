#!/usr/bin/env/ python3.8

import socket

host = "localhost" #127.0.0.1
port = 80

s = socket.getaddrinfo(host, port, family=socket.AF_INET, proto=socket.IPPROTO_TCP)
print(s)

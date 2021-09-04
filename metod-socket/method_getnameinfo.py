#!/usr/bin/env python3.8

import socket

# method getnameinfo(value_tuple) melakukan pencarian DNS(domain name server) untuk
# mengambil representasi teks yang sesuai dengan IP, Port, Service(layanan)

# Syntax
# socket.getnameinfo(value_tuple)

# Parameter Value
# value tuple -> (host, port)

host = "127.0.0.1" # localhost
addr = (host, 22)  # 22 adalah port [20, 21, 22, 80, 443 ..., ...]

#======================================================

# menggunakan argument socket.NI_NOFQDN
# untuk menampilkan nama domain dan nama service(layanan) pada port tertentu

a = socket.getnameinfo(addr, socket.NI_NOFQDN)
print(a)

#======================================================

# menggunakan argument socket.NI_NUMERICHOST
# untuk menampilkan ip dan nama service(layanan) pada port tertentu

# contoh menggunakan port 80
b = socket.getnameinfo((host, 80), socket.NI_NUMERICHOST)
print(b)

#======================================================

# menggunakan argument socket.NI_NUMERICSERV)
# untuk menampilkan nama domain dan nilai portnya 

c = socket.getnameinfo(addr, socket.NI_NUMERICSERV)
print(c)

#=======================================================

# menggunakan argument socket.NI_NAMEREQD
# untuk menampilkan nama domain dan nama service(layanan) pada port tertentu

# contoh menggunakan port 443
d = socket.getnameinfo((host, 443), socekt.NI_NAMEREQD)
print(d)



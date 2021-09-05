#!/usr/bin/env python3.8

import socket

# sesuai IPv4, alamat IP adalah nomor 32-bit. alamat IPv4 ini direpresentasikan
# sebagai empat angka desimal. setiap angak dipisahkan oleh titik dan setiap
# angka berkisar dari 0 - 255.


# method inet_aton() mengubah alamat IPv4 dari format string
# menjadi format biner 32-bit yang dikemas.

# format biner yang dikembalikan dapat diteruskan ke program apapun 
# yang memerlukan alamat IP sebagai objek tipe C struct in_addr.

# Syntax
# socket.inet_aton(value)

# Parameter Value
# ip address, yang perlu dikonversi dari format dotted-quad
# string menjadi format biner 32-bit.

ip = "127.0.0.1"
s = socket.inet_aton(ip)
print(s)

#!/usr/bin/env python3.8

import socket
import struct


# method inet_ntoa() mengkonversi alamat ip yang dalam format 32-bit
# dikemas ke format string 0.0.0.0 yang dapat dibaca manusia

# Syntax
# socket.inet_ntoa(value)

# Parameter Value
# ip address, alamat dalam format 34-bit yang akan di konversi
# mengembalikan alamat ip dalam format quad-string bertitik

angka = 192168150

# method struct.pack() digunakan untuk mengubah tipe data menjadi byte
# parameter !(network) I(bilangan bulat)

s_32bit = struck.pack('!I', angka)
s = socket.inet_ntoa(s_32bit)
print(s)



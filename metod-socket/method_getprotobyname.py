#!/usr/bin/env python3.8

import socket

# method getprotobyname() mengambil string protokol seperti TCP
# UDP atau ICMP dan mengembalikan konstanta terkait untuk protokol
# seperti yang didefinisikan oleh modul socket

# -----------------------------------------------------------------

# misalnya untuk TCP getprotobyname() mengembalikan nilai konstan 6
# dan untuk UDP konstanta yang dikembalikan oleh getprotobyname()
# adalah 17 dan ICMP nilai konstanta yang dikembalikan adalah 7

# -----------------------------------------------------------------

# nilai yang dikembalikan dapat digunakan sebagai nilai
# untuk parameter ke-3 bernama proto dari modul socket menggunakan parameter

# Syntax
# socket.getprotobyname(value)

# Parameter Value
# nama protokol TCP, UDP, ICMP


# menggunakan protokol TCP
protokol_tcp = "TCP"
stcp = socket.getprotobyname(protokol_tcp)
print(f"konstanta socket terkait dengan protokol: {protokol_tcp} adalah {stcp}")


# menggunakan protokol UDP
protokol_udp = "UDP"
sudp = socket.getprotobyname(protokol_udp)
print(f"konstanta socket terkait dengan protokol: {protokol_udp} adalah {sudp}")

# menggunakan protokol ICMP
protokol_icmp = "ICMP"
sicmp = socket.getprotobyname(protokol_icmp)
print(f"konstanta socket terkait dengan protokol: {protokol_icmp} adalah {sicmp}")


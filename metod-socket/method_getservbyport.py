#!/usr/bin/env python3.8

import socket

# method getservbyport() mengembalikan nama layanan untuk nomor port tertentu.
# seiring nomor port, nama protokol - 'tcp' atau 'udp' perlu ditentukan sebagai nilai
# untuk parameter kedua untuk mendapatkan getservbyport()

# syntax
# socket.getservbyport(value, name)

# Parameter value
# nomor port dan nama protokol tcp/udp

# contoh program

for port in range(20, 200):
    
    # melooping dari rentan nilai 20 - 200
    # keyword try except <type error> menangkap error 
    try:
        nama_layanan = socket.getservbyport(port, 'tcp') # menggunakan protokol 'tcp'
        print(f"port: {port}    service: {nama_layanan}")
    except OSError:
        pass
        


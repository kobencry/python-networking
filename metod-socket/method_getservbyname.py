#!/usr/bin/env python3.8

import socket

# method getservbyname() mengambil nama service(layanan) jaringan dan nama protokol
# yang mendasarinya dan mengembalikan nomor port tempat service(layanan) didefinisikan
# oleh /etc/services. yang dimaksud dengan layanan jaringan adalah protokol
# aplikasi seperti http atau ftp. protokol yang mendasarinya adalah protokol
# transport layer seperti tcp atau udp.

# Syntax
# socket.getservbyname(nama layanan, protokol)

# Parameter Value
# nama layanan     protokol 'tcp'/'udp' 


nama_layanan = [
        'daytime',
        'ftp-data',
        'ftp',
        'ssh',
        'telnet',
        'smtp',
        'time',
        'gopher',
        'http',
        'kerberos',
        'pop2',
        'pop3',
        'netbios-ns',
        'netbios-ssn',
        'imap',
        'sql-net',
        'sqlserv',
        'irc']

for nama in nama_layanan:
    # keyword try except <type error>  menangkap error
    try:
        port = socket.getservbyname(nama, 'tcp')
        print(f"nama service: {nama}  port: {port}")
    
    except OSError:
        print(f"nama service {nama} tidak ada")




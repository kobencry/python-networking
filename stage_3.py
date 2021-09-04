import os
import socket

class Sniffing:
    def __init__(self, host):
        self.host = host

    def attack(self):
        if os.name == 'nt':
            protocol = socket.IPPROTO_IP
        else:
            protocol = socket.IPPROTO_ICMP

        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, protocol)
        s.bind((self.host, 0))
        s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        print(s.recvfrom(65565))

        if os.name =='nt':
            s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

if __name__=='__main__':
    host = input("set HOST> ")
    snif = Sniffing(host)
    snif.attack()


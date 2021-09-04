import time
import socket

class Terminal:
    def __init__(self, username='root', hostname=socket.gethostname()):
        self.username = username
        self.hostname = hostname

    def __repr__(self):
        return f"{self.username}@{self.hostname}~#: "

    def __str__(self):
        return self.__repr__()

if __name__=='__name__':
    username = input('username: ')
    hostname = input('hostname: ')
    terminal = Terminal(username, hostname)
    print(terminal)


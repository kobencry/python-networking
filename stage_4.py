import time
import socket

class Terminal:
	def __init__(self, username='root', hostname=socket.gethostname()):
		self.username = username
		self.hostname = hostname
	
	def __repr__(self):
		return f"{self.ursername}@{self.hostname}~#: "
	
	def __str__(self):
		return self.__repr__()

terminal = Terminal()
print(terminal)

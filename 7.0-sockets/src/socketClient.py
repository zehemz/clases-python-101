'''
https://wiki.python.org/moin/HowTo/Sockets
'''
import socket
# crea un socket INET de tipo STREAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ahora se conecta al servidor web en el puerto 80 (http)
s.connect(("www.mcmillan-inc.com", 80))

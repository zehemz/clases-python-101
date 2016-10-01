'''
socket server
'''
import socket
# crea un socket INET de tipo STREAM
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# asocia el socket a un host público
# y aun puerto bien conocido
serversocket.bind((socket.gethostname(), 80))
'''
Si hubiera usado s.bind(('', 80)) or s.bind(('localhost', 80)) or s.bind(('127.0.0.1', 80)) también tendría un socket servidor, pero solo sería accesible desde la misma máquina
'''

# lo convierte en socket servidor
serversocket.listen(5)

while True:
    # acepta conexiones externas
    (clientsocket, address) = serversocket.accept()
    # ahora se trata el socket cliente
    # en este caso, se trata de un servir multihilado
    ct = client_thread(clientesocket)
    ct.run()

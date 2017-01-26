#this is used simply to test the honeypot by sending and receiving data

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 3389))
sock.sendall('helloello')

print sock.recv(16)
sock.close()
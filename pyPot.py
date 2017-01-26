import socket
from scapy.all import *
import thread

rdp = {'port': 3389, 'responses' : ('resp1', 'resp2', 'resp3'), 'timeout' : 30}

#protocols = ('rdp', 'ftp', 'http', 'ntp')
protocols = (rdp,)


for protocol in protocols:


    sniffedData = sniff(count=0, timeout=5)
    print sniffedData











    # print protocol['port']
    # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # sock.bind(('localhost', protocol['port']))
    # sock.listen(10)
    # while True:
    #     print 'Waiting for connection on port ' + str(protocol['port'])
    #     connection, clientAddress = sock.accept()
    #     recvData = connection.recv(4096)
    #     if recvData:
    #         print recvData
    #         recvData = ''

print 'fin'
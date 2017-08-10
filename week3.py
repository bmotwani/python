
import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('www.data.pr4e.org', 80))
mysocket.send('GET http://data.pr4e.org/intro-short.txt HTTP/1.0\n\n'.encode())

while True:
    data = mysocket.recv(512)
    if len(data) < 1: break
    print(data.decode())
    
mysocket.close()
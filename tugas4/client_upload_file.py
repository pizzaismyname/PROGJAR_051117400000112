import socket
import base64
import os

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 8888)
print(f"connecting to {server_address}")
sock.connect(server_address)

try:
    command = ("upload ")
    filename = input("enter filename: ")
    try:
        f = open(filename, 'rb')
    except:
        print("cannot open file")
    else:
        length = len(filename) + 1
        content = base64.encodestring(f.read())
        f.close()
        f = open("temp","wb")
        f.write(content)
        f.close()
        f = open("temp","rb")
        data = command.encode() + filename.encode() + (b" ") + f.read(1024)
        print(data)
        while (data):
            sock.send(data)
            data = f.read(1024)
            response = sock.recv(1024)
        print(response)
        os.remove("temp")
finally:
    print("closing")
    sock.close()

import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 31000)
print(f"connecting to {server_address}")
sock.connect(server_address)

try:
    filename = 'file.txt'
    f = open(filename, 'rb')
    length = f.read(1024)
    while length:
        sock.send(length)
        length = f.read(1024)
    f.close()
finally:
    print("closing")
    sock.close()

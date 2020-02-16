import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 31000)
print("connecting to", server_address)
sock.connect(server_address)

try:
    filename = input("enter file name: ")
    # Send file
    try:
        f = open(filename, 'rb')
    except:
        print("cannot open file")
    else:
        length = f.read(1024)
        while length:
            sock.send(length)
            length = f.read(1024)
        f.close()
finally:
    print("closing")
    sock.close()

import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 31000)
print("connecting to", server_address)
sock.connect(server_address)

try:
    # Send filename
    filename = input("enter filename: ")
    print("sending file name:", filename)
    sock.sendall(filename.encode())
    # Receive file
    with open('received_file', 'wb') as f:
        while True:
            data = sock.recv(1024)
            if not data:
                break
            # Write data to a file
            f.write(data)
    f.close()
finally:
    print("closing")
    sock.close()

import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
sock.bind(('127.0.0.1', 10000))
# Listen for incoming connections
sock.listen(1)
while True:
    # Wait for a connection
    print("waiting for a connection")
    connection, client_address = sock.accept()
    print(f"connection from {client_address}")
    # Receive filename
    filename = connection.recv(32)
    try:
        f = open(filename, 'rb')
    except:
        print("cannot open file")
    else:
        length = f.read(1024)
        while length:
            connection.send(length)
            length = f.read(1024)
        f.close()
    # Clean up the connection
    connection.close()

import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 31000)
print(f"connecting to {server_address}")
sock.connect(server_address)

try:
    # Send data
    filename = input("Masukkan nama file: ")
    print("sending file name:", filename)
    sock.sendall(filename.encode())
    # # Look for the response
    # amount_received = 0
    # amount_expected = len(filename)
    # while amount_received < amount_expected:
    #     data = sock.recv(16)
    #     amount_received += len(data)

    with open('received_file', 'wb') as f:
        while True:
            data = sock.recv(1024)
            if not data:
                break
            # write data to a file
            f.write(data)
    f.close()
finally:
    print("closing")
    sock.close()

import sys
import socket
import _thread


# Define a function for the thread
def create_socket(TCP_PORT):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind the socket to the port
    server_address = ('127.0.0.1', TCP_PORT)
    print(f"starting up on {server_address}")
    sock.bind(('127.0.0.1', TCP_PORT))
    # Listen for incoming connections
    sock.listen(1)
    while True:
        # Wait for a connection
        print("waiting for a connection")
        connection, client_address = sock.accept()
        print(f"connection from {client_address}")
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(32)
            print(f"received {data}")
            if data:
                print("sending back data")
                connection.sendall(data)
            else:
                print(f"no more data from {client_address}")
                break
        # Clean up the connection
        connection.close()
try:
    _thread.start_new_thread(create_socket, (31000, ))
    _thread.start_new_thread(create_socket, (31001, ))
    _thread.start_new_thread(create_socket, (31002, ))
finally:
    while 1:
        pass

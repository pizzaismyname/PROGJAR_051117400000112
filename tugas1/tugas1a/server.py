import sys
import socket
import _thread


# Define a function for the thread
def create_socket(TCP_PORT):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind the socket to the port
    sock.bind(('127.0.0.1', TCP_PORT))
    # Listen for incoming connections
    sock.listen(1)
    while True:
        # Wait for a connection
        print("waiting for a connection")
        connection, client_address = sock.accept()
        print(f"connection from {client_address}")
        # Receive the data in small chunks and retransmit it
        with open('received_file', 'wb') as f:
            while True:
                data = connection.recv(1024)
                if not data:
                    break
                # write data to a file
                f.write(data)
        f.close()
        # Clean up the connection
        connection.close()


try:
    _thread.start_new_thread(create_socket, (31000, ))
    _thread.start_new_thread(create_socket, (31001, ))
    _thread.start_new_thread(create_socket, (31002, ))
finally:
    while 1:
        pass
import socket
import threading
# Define server host and port
HOST = '127.0.0.1'  # Localhost
PORT = 8080         # Port to listen on

#making the server has the ability to handle multi connections
def handle_client(conn, addr):
    print(f"New connection: {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            break  # If no data is received, close the connection
        print(f"Message from {addr}: {data.decode()}")
    conn.close()
    print(f"Connection with {addr} closed")
# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_socket.bind((HOST, PORT))

# Listen for incoming connections (max 5 in the queue)
server_socket.listen(5)
print(f"Server is listening on {HOST}:{PORT}...")

# Accept a connection
while True:
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    # Create a new thread for each client
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
    print(f"Active connections: {threading.active_Count() - 1}")

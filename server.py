import socket

# Define server host and port
HOST = '127.0.0.1'  # Localhost
PORT = 8080         # Port to listen on

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_socket.bind((HOST, PORT))

# Listen for incoming connections (max 5 in the queue)
server_socket.listen(5)
print(f"Server is listening on {HOST}:{PORT}...")

# Accept a connection
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

# Receive data from the client
data = conn.recv(1024)
print(f"Message from client: {data.decode()}")

# Close the connection
conn.close()
server_socket.close()

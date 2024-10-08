import socket

# Define server host and port
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 8080         # The port used by the server



# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

# Send a message to the server
message = "Hello from the client!"
client_socket.sendall(message.encode())
print("Message sent to server")

# Close the socket
client_socket.close()

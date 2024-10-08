import socket
import threading
import os
# Define server host and port
HOST = '127.0.0.1'  # Localhost
PORT = 8080         # Port to listen on

#files transfer by the server
def handle_client(conn, addr):
    print(f"New connection: {addr}")
    
    while True:
        # receiving the name of the file 
        file_request = conn.recv(1024).decode()
        if not file_request:
            break  # If no data is received, close the connection

        print(f"Client {addr} requested the file: {file_request}")
        
        print("Files in current directory:", os.listdir())
        # verify if the file exists
        if os.path.exists(file_request):
            # sending the confirmation
            conn.send("File found".encode())

            # open the file and sending it into chunks
            with open(file_request, 'rb') as file:
                chunk = file.read(1024)
                while chunk:
                    conn.send(chunk)
                    chunk = file.read(1024)
            print(f"File {file_request} sent successfully to {addr}")
        else:
            # inform the client that the file does not exist
            conn.send("File not found".encode())
    
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

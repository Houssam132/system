import socket

# Define server address and port
HOST = '127.0.0.1'  # Server IP address (localhost for local testing)
PORT = 8080         # Server port

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))
# Request the file from the user
file_request = input("Enter the name of the file you want to download: ")

# Send the file request to the server
client_socket.send(file_request.encode())

# Receive server's response (if the file exists or not)
server_response = client_socket.recv(1024).decode()

if server_response == "File found":
    print(f"Downloading {file_request}...")
    with open(f"downloaded_{file_request}", 'wb') as file:
        while True:
            # Receive data in chunks of 1024 bytes
            chunk = client_socket.recv(1024)
            if not chunk:
                break  # If no more data, exit the loop
            print(f"Received chunk: {len(chunk)} bytes")  # Debugging line
            file.write(chunk)  # Write the chunk to a file
            file.flush()  # Ensure data is written to disk immediately
    print(f"File {file_request} downloaded successfully!")
else:
    print("File not found on the server.")

# Close the connection
client_socket.close()

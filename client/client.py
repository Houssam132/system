import socket

# Define server host and port
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 8080         # The port used by the server

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))
#asking for the name of the file
file_request=input("enter the name of the file you want to download /n")
client_socket.send(file_request.encode())

# receiving the response by the server(if the file exists or not)
response = client_socket.recv(1024).decode()

if response == "File found":
    # create local storage for the file
    with open(f"downloaded_{file_request}", 'wb') as file:
        print(f"Downloading {file_request}...")
        while True:
            # receiving the chunks
            chunk = client_socket.recv(1024)
            if not chunk:
                break
            file.write(chunk)
            print(f"Received chunk: {len(chunk)} bytes")    
    file.close()
    print(f"File {file_request} downloaded successfully!")
else:
    print("File not found on the server.")


# Close the socket
client_socket.close()

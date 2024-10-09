import socket

# Define server host and port
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 8080         # The port used by the server

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))
action=("type 'download' or 'upload'")
if action=='download':                             
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

elif action=='upload':
    # File upload logic
    file_to_upload = input("Enter the name of the file you want to upload: ")
    try:
        # Open the file to be uploaded
        with open(file_to_upload, 'rb') as file:
            # Notify the server of the upload request
            client_socket.send(f"UPLOAD:{file_to_upload}".encode())
            # Wait for the server to confirm it can receive the file
            response = client_socket.recv(1024).decode()
            if response == "Ready to receive":
                print(f"Uploading {file_to_upload}...")

                # Send the file in chunks
                while True:
                    chunk = file.read(1024)
                    if not chunk:
                        break
                    client_socket.send(chunk)
     # Notify the server that the file is fully uploaded
                client_socket.send(b"END_OF_FILE")
                print(f"File {file_to_upload} uploaded successfully!")

    except FileNotFoundError:
        print(f"File {file_to_upload} not found. Please check the file name and try again.")
else:
    print("Invalid action. Please type 'upload' or 'download'.")

# Close the socket
client_socket.close()

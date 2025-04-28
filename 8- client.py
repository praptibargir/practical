import socket

Server_ip = "localhost"
Server_host = 8002
FORMAT = "utf-8"

CS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
CS.connect((Server_ip, Server_host))

# Open and read file
file_path = "abc.txt"
file = open(file_path, "r")
data = file.read()
file.close()

# Send file name
CS.send(file_path.encode(FORMAT))
print("File name sent to server.")
msg = CS.recv(1024).decode(FORMAT)
print(f"Server: {msg}")

# Send file data
CS.send(data.encode(FORMAT))
print("File data sent to server.")
msg = CS.recv(1024).decode(FORMAT)
print(f"Server: {msg}")

CS.close()

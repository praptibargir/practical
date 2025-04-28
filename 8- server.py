import socket

Server_ip = "localhost"
Server_host = 8002
FORMAT = "utf-8"

SS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SS.bind((Server_ip, Server_host))
SS.listen(5)

print("🔌 Server is listening for incoming connections...")

s1, addr = SS.accept()
print(f"Connected with {addr}")

# Receive file name
file_name = s1.recv(1024).decode(FORMAT)
print(f"File name received: {file_name}")
s1.send("File name received".encode(FORMAT))

# Receive file data
data = s1.recv(1024).decode(FORMAT)
print("File data received from client.")
s1.send("File data received".encode(FORMAT))

# Save to file
file = open(file_name, "w")
file.write(data)
file.close()
print(f"File '{file_name}' saved successfully.")

s1.close()
SS.close()

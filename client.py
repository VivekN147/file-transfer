import socket

s = socket.socket()
host = input(str("Please Enter the Host Address of the Sender : "))
port = 8080
s.connect((host, port))
print("Connected...")

filename = input(str("Please Enter a Filename for the incoming File : "))
file = open(filename, 'wb')
file_data = s.recv(1024)
file.write(file_data)
file.close()
print("File has been Received Successfully.")

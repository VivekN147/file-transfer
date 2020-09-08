# create a simple file transfer program using python
import socket

s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host, port))
s.listen(1)
print(host)
print("Waiting for any incoming Connections...")
conn, addr = s.accept()
print(addr, "Has Connected to the Server.")

filename = input(str("Please Enter the Filename of the File : "))
file = open(filename, 'rb')
file_data = file.read(1024)
conn.send(file_data)
print("Data has been Transmitted Successfully.")

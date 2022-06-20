import socket
SV = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST = ""
PORT = 12345
SV.bind((HOST,PORT))
SV.listen(5)
print("listen")
CONN,ADDR = SV.accept()
print(str(CONN) + str(ADDR))
while True:
    HU = input("Server: ")
    CONN.sendall(HU.encode())
    HS = CONN.recv(1024)
    print("Client: " + str(HS.decode()))
    if HU == "Q":
        print("quiting now")
        SV.close()
        

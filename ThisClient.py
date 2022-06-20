import socket
import atexit
HOST = "localhost"
PORT = 12345
CV = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
def EXIT():
    print("this runs after keyboard interupt")
    CV.close()
atexit.register(EXIT)
CV.connect((HOST,PORT))
print("connected")
while True:
    CS = CV.recv(1024)
    print("Server: " + str(CS.decode()))
    CU = input("client: ")
    CV.sendall(CU.encode())
    if CU == "Q":
        CV.close()

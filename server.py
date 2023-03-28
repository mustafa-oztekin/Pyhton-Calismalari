import socket
import time
import keyboard
"""
import pickle
headersize = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
print(socket.gethostname())
s.listen(5)
while True:
    clientsocket, addr = s.accept()
    print(f"connettion from {addr} has been established!")
    data = {1: "hey", 2: "there"}
    msg = pickle.dumps(data)
    msg = bytes(f'{len(msg):<{headersize}}', "utf-8") + msg
    clientsocket.send(msg)
"""
headersize = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)
print("Server is running now...")

while True:
    client_socket, address = s.accept()
    print(f"Connection from {address} bas been established!")
    full_msg = ''
    new_msg = True
    while True:
        time.sleep(3)
        msg = "server mesaj yolladi..."
        msg = f"{len(msg):<{headersize}}" + msg
        client_socket.send(bytes(msg, "utf-8"))
        if keyboard.is_pressed("q"):
            print("q pressed, ending loop")
            break
        
    kapat = "kapat"
    kapat = f"{len(kapat):<{headersize}}" + kapat
    client_socket.send(bytes(kapat, "utf-8"))
    break

        #while True:
        #    yeni_msg = client_socket.recv(16)
        #    if new_msg:
        #        print(f"new msg length: {yeni_msg[:headersize]}")
        #        msglen = int(yeni_msg[:headersize])
        #        new_msg = False

        #    full_msg += yeni_msg   #.decode("utf-8")

        #    if len(full_msg) - headersize == msglen:
        #        print("full msg received")
        #        print(full_msg[headersize:])
        #        new_msg = True
        #        full_msg = ''
        #        break
        #time.sleep(3)

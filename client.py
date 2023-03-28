import socket
#import pickle

headersize = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))
#print(socket.gethostname())

while True:
  full_msg = ''
  new_msg = True
  while True:
    msg = s.recv(16)
    if new_msg:
      print(f"new msg length: {msg[:headersize]}")
      msglen = int(msg[:headersize])
      new_msg = False

    full_msg += msg.decode("utf-8")
    #full_msg += msg

    if len(full_msg) - headersize == msglen:
      print("full msg received")
      print(full_msg[headersize:])
      son = full_msg[headersize:]
      new_msg = True
      full_msg = ''
      if son == "kapat":
        break
  s.close()
  break
      #data = pickle.loads(full_msg[headersize:])
      #print(data)


      #yeni_msg = f"{len(full_msg[headersize:]):<{headersize}}" + full_msg[headersize:]
      #s.send(bytes(yeni_msg, "utf-8"))
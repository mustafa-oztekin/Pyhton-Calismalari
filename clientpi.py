import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("pi", 5000))
    

msg = 'farklı internet bağlantılarından veri gönderiyorum...'
s.send(bytes(msg, "utf-8"))
    
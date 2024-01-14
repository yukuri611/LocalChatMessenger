import socket
import os

#ソケットドメイン（使用する通信の形式）と、ソケットタイプ(アプリケーションの通信する方法)を指定
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = "./socket_file"

#ここで、以前の接続のunlink処理を行う
try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

sock.bind(server_address)

sock.listen(1)

while True:
    print("Waiting for connection")
    connection, client_address = sock.accept()
    print(client_address)
    print("Connected to {}".format(client_address))

    data  = connection.recv(16).decode("utf-8")
    print("Received: "+data)
    message = input("What do you want to send?")

    connection.sendall(message.encode())

    connection.close()
    print("Current connection has closed")
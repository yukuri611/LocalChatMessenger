import socket

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = "./socket_file"

#接続を試みる。後でtry処理でエラーに対応
sock.connect(server_address)
print("connected to the server!")

#メッセージの送信
message = input("What do you want to send?")
sock.sendall(message.encode())
print("Message has been sent!")

data = str(sock.recv(32))

print(data)

sock.close()

print("socket has closed")
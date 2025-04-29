# client.py - 채팅 클라이언트
from socket import *
import threading

port = 3333
BUFFSIZE = 1024

def recv_msg(sock):
    while True:
        try:
            data = sock.recv(BUFFSIZE)
            if not data:
                break
            print("\n📩", data.decode())
        except:
            break

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', port))

thread = threading.Thread(target=recv_msg, args=(sock,))
thread.daemon = True
thread.start()

while True:
    msg = input("📝 메시지 입력: ")
    if msg == 'quit':
        break
    sock.send(msg.encode())

sock.close()

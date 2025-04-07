import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9000))
s.listen(1)

while True:
    client, addr = s.accept()
    print('Connection from', addr)

    name = client.recv(1024).decode()
    print('Received name:', name)

    student_id = 20201502
    client.send(student_id.to_bytes(4, 'big'))

    client.close()

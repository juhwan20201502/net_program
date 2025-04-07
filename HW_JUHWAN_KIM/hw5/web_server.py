from socket import *
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

mime_types = {
    'html': 'text/html',
    'png': 'image/png',
    'ico': 'image/x-icon'
}

s = socket()
s.bind(('', 8081))
s.listen(10)
print("✅ 웹 서버 실행 중 (포트 8081)...")

while True:
    c, addr = s.accept()
    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')

    if len(req) < 1:
        c.close()
        continue

    print(f"🌐 요청: {req[0]}")
    try:
        filename = req[0].split()[1][1:]
    except:
        c.close()
        continue

    if filename == '':
        filename = 'index.html'

    if os.path.exists(filename):
        ext = filename.split('.')[-1]
        mimeType = mime_types.get(ext, 'application/octet-stream')
        header = 'HTTP/1.1 200 OK\r\n'
        header += 'Content-Type: ' + mimeType + '\r\n\r\n'
        c.send(header.encode())

        # 🔥 여기 수정됨! ↓↓↓
        if ext == 'html':
            with open(filename, 'r', encoding='utf-8') as f:
                data = f.read()
                c.send(data.encode('euc-kr'))  # 웹에서 한글 보기 좋게 euc-kr로 전송
        else:
            with open(filename, 'rb') as f:
                data = f.read()
                c.send(data)
    else:
        header = 'HTTP/1.1 404 Not Found\r\n\r\n'
        body = '<HTML><HEAD><TITLE>Not Found</TITLE></HEAD><BODY>Not Found</BODY></HTML>'
        c.send(header.encode())
        c.send(body.encode())

    c.close()

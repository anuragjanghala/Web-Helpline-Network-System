import socket

HEADER_SIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 8086))
full_msg = ""
new_msg = True
while True:
    msg = s.recv(16)
    if new_msg:
        print(f"new message length: {msg[:HEADER_SIZE]}")
        msglen = int(msg[:HEADER_SIZE])
        new_msg = False

    full_msg += msg.decode("utf-8")

    if len(full_msg)-HEADER_SIZE == msglen:
        print(full_msg[HEADER_SIZE:])
        new_msg = True
        break
filename = input(str("enter file to be transfer: "))
file = open(filename, 'rb')
file_data = file.read(1024)
s.send(file_data)
print("Data file transfered successfully!")
file.close()

s.close()

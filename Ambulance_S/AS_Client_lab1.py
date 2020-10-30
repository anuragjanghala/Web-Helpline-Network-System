import socket

fichier = open(f"Record/list1.txt","r")
string = fichier.read()
pos1 = string.find(f'Version : ')
versionnb = string[pos1+10:pos1+13]
vnbClient = int(versionnb)
fichier.close()

serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverPort = 9351
serverSocket.connect((socket.gethostname(),serverPort))
MAXSIZE = 10

print(f'Connection established')
serverSocket.send(f"{versionnb}".encode())
msg1 = serverSocket.recv(1024)
print(f'Answer from the webserver: \r\n {msg1}')
serverSocket.send(f"GET /list1.html HTTP/1.1\r\nConnection : Close\r\n\r\n".encode()) 
msg1 = serverSocket.recv(1024)
print(f'Answer from the webserver: \r\n {msg1}')
serverSocket.send(f"Waiting for the file".encode())
html_object = ''
newobj = True
obj = True
while obj:
	msg2 = serverSocket.recv(1024)
	if newobj and len(msg2)!=0:
		objlength = int(msg2[:MAXSIZE])
		newobj = False
	html_object += msg2.decode()
	if len(html_object)-MAXSIZE > objlength:
		print(f'Received Message:\r\n{html_object[MAXSIZE:]}')
		print(f'Length received Message:{len(html_object)}')
		if (len(html_object)>40):
			fichier = open(f"Record/list1.txt","w")
			fichier.write(f'{html_object[MAXSIZE:]}')
			fichier.close()
			content = str(html_object[MAXSIZE:])
			pos1 = content.find('Version : ')
			vnbServer = int(content[pos1+10:pos1+13])
			print(f'Version of the server:{vnbServer}\r\n')
			html_object = ''
			obj = False
		else:
			html_object = ''
			obj = False
			vnbServer = vnbClient
serverSocket.close()  

for i in range(vnbClient+1,vnbServer+1):
	serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	serverSocket.connect((socket.gethostname(),serverPort))
	serverSocket.send(f"GET /person{i}.html HTTP/1.1\r\nConnection : Close\r\n\r\n".encode())
	msg1 = serverSocket.recv(1024)
	print(f'Answer from the webserver: \r\n {msg1}')
	serverSocket.send("Waiting for the file".encode())
	html_object = ''
	newobj = True
	obj = True
	while obj:
		msg2 = serverSocket.recv(1024)
		if newobj and len(msg2)!=0:
			objlength = int(msg2[:MAXSIZE])
			newobj = False
		html_object += msg2.decode()
		if len(html_object)-MAXSIZE > objlength:
			print(f'Received Message:\r\n{html_object[MAXSIZE:]}')
			fichier1 = open(f"Record/person{i}_1.txt","w")
			fichier1.write(f'{html_object[MAXSIZE:]}')
			fichier1.close()

			html_object = ''
			obj = False
	serverSocket.close()  
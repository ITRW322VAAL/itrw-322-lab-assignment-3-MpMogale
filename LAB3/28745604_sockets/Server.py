import 

Host = '127.0.0.1'
PORT = 9999

with socket.socket(socke.AF_INET,socket.SOCK_SREAM) as s:
	s.bind((HOST,PORT))
	s.listen()
	with conn:
		print('Server is connected with address,addr')
		while True:
			data = conn.recv(2848)
			if not data:
				break
			conn.sendall(data)
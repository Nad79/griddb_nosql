import socket, sys
host = ''
port = 12800
#création d'un socket
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#liaison d'un socket au tuple hote, port
try:
	mySocket.bind((host,port))
except  socket.error:
	print ("Echec de connexion du socket à l'adresse choisie")
	sys.exit()
while True:
	#En attente de la connexion du client
	print("Serveur prêt en attente de connexion")
	mySocket.listen(5)
	connexion, adresse = mySocket.accept()
	
	print(f"client connecté a l'adresse : {adresse}")
	#dialogue avec le clilent
	connexion.send(b"5/5")
	msgClient  = connexion.recv(1024)
	print (f">{msgClient}")
	while 1:
		print (f"C> {msgClient}")
		if msgClient.upper() == "FIN" or msgClient == "":
		    break
		msgServeur = input(">")
		connexion.send(msgServeur.encode())
		msgClient = connexion.recv(1024)
	#fermeture de la connexion
	connexion.send("au revoir")
	connexion.close()

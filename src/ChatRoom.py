# newMessage() is called by a Client object when a new message is received from its associated IMClient
# updateConnected() will broadcast messages stored inside the messageQueue to the list of
# connectedClients when a new entry in ther queue is detected

from Client import Client
from queue import Queue


class ChatRoom:
	
	def __init__(self):
		self.chatRoomRunning = True
		self.name = ""
		self.clientsConnected = []
		self.messageQueue = []
		self.startLoop()

	def newClient(self, newClient):
		''' called by IMServer, newClient is of type Client '''
		self.clientsConnected.append(newClient)
		return 

	def newMessage(self, messageIn, clientName):
		''' called by the Client object '''
		newMessage = clientName + " : " + messageIn
		self.messageQueue.put(newMessage)
		return
	
	def updateConnectedClients(self, messageIn):
		# loop through all clients updating them 
		for client in clientsConnected:
			client.sendMessageUpdate(messageIn)
		return
	
	def startLoop(self):
		''' Is called once ChatRoom is initted '''
		queueHandler = threading._start_new_thread(mainLoop, ())
		return

	def mainLoop(self):
		# get is blocking by default (yay) 
		while self.chatRoomRunning:
			messToBroadcast = messageQueue.get()
			self.updateConnectedClients(messToBroadcast)
		return 
# newMessage() is called by a Client object when a new message is received from its associated IMClient
# updateConnected() will broadcast messages stored inside the messageQueue to the list of
# connectedClients when a new entry in ther queue is detected

from Client import Client
from Queue import Queue
import threading


class ChatRoom:

	def __init__(self, name):
		self.chatRoomRunning = True
		self.name = name
		self.clientsConnected = []
		self.messageQueue = Queue()
		self.startLoop()

	def newClient(self, newClient):
		''' called by IMServer, newClient is of type Client '''
		self.clientsConnected.append(newClient)

	def specialMessage(self, message):
		if message[0] is '/':
			return True

	def ignoreFirstWord(self, message):
		return message.split(' ', 1)[1]

	def userJoining(self, message):
		if message.split(" ")[0] == "/announce":
			return True

	def newMessage(self, messageIn, clientName):
		''' called by the Client object '''
		if self.specialMessage(messageIn):
			if self.userJoining(messageIn):
				newMessage = clientName + self.ignoreFirstWord(messageIn)
		else:
			newMessage = clientName + " : " + messageIn
		self.messageQueue.put(newMessage)
		print "(%s) %s" % (self.name, newMessage)

	def updateConnectedClients(self, messageIn):
		# loop through all clients updating them
		for client in self.clientsConnected:
			client.sendMessageUpdateToIMClient(messageIn)

	def startLoop(self):
		''' Is called once ChatRoom is initted '''
		queueHandler = threading._start_new_thread(self.mainLoop, ())
		return

	def mainLoop(self):
		# get is blocking by default (yay)
		while self.chatRoomRunning:
			messToBroadcast = self.messageQueue.get()
			self.updateConnectedClients(messToBroadcast)
		return 
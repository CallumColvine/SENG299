#!/usr/bin/env python3 

# newMessage() is called by a Client object when a new message is received from its associated IMClient
# updateConnected() will broadcast messages stored inside the messageQueue to the list of
# connectedClients when a new entry in ther queue is detected

class ChatRoom:
	
	def __init__(self):
		self.name = ""
		self.clientsConnected = []
		self.messageQueue = []

	def newClient(self, newClient):
		raise NotImplementedError

	def newMessage(self, messageIn, clientName):
		return ""
	
	def updateConnectedClients(self, messageIn):
		return ""
	
	def mainLoop():
		raise NotImplementedError
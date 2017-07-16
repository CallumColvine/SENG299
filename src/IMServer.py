#!/usr/bin/env python3 

# Loops, listening for new IMClients wanting to enter a ChatRoom
# Keep a list of Client objects for each IMClient and a list for existing ChatRooms
class IMServer: 

	def __init__(self):
		self.chatRooms = []
		self.connectedClients = []

	def createChatRoom(self, roomName):
		raise NotImplementedError
	
	def listenForConnections(self):
		raise NotImplementedError
	
	def addNewClient(clientName, clientIP, clientPort):
		raise NotImplementedError

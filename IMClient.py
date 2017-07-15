#!/usr/bin/env python3 

# Initializes connections with IMServer with initConnection()
# These connections are passed on to a Client object which is managed by IMServer 
class IMClient: 

	def __init__(self):
		self.username = ""
		self.curChatRoom = ""
		self.port = -1

	def initConnection(self, ip, port):
		return true
	
	def updateChat(self, newMessage):
		raise NotImplementedError 
	
	def listenForInput(self):
		return ""
	
	def sendInput(self, messtoSend):
		return true

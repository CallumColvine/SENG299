#!/usr/bin/env python3 

# One-to-one relationship with IMClients
# Constantly listening for new messages broadcast by the IMClient
# 	Calls its writeMessage() function when a new message is received 
# 	writeMessage() calls the ChatRoom.newMessage() function
class Client:

	def __init__(self):
		self.ip = ""
		self.port = -1
		self.curChat = ChatRoom(self) # I dont know if this is entirely valid
		self.name = ""

	def listenForMessage(self):
		return ""
	
	def writeMessage(self, messageIn):
		return true
	
	def sendMessageUpdate(self, newMessage):
		return true
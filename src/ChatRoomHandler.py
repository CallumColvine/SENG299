from ChatRoom import ChatRoom


class ChatRoomHandler(object):

	def __init__(self):	
		self.chatRoomList = []
		self.initChatRooms()

	def initChatRooms(self):
		self.createChatRoom("General")
		self.createChatRoom("Random")	
		return

	def addClient(self, roomName, clientObj):
		''' Returns the ChatRoom obj so the Client can keep reference to it '''
		for room in self.chatRoomList:
			if room.name == roomName:
				room.newClient(clientObj)
				return room
		print "ChatRoomHandler: unable to find specified ChatRoom", roomName
		return None

	def removeClient(self, roomName):
		for room in self.chatRoomList:
			if room.name == roomName:
				room.newClient(clientObj)		
		return

	def createChatRoom(self, roomName):
		# Avoid duplicates
		for room in self.chatRoomList:
			if room.name == roomName:
				return
		print "Appending lists"
		tempRoom = ChatRoom(roomName)
		self.chatRoomList.append(tempRoom)
		return


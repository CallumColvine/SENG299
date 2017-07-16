import Queue
import select
import socket
import sys
import threading

host = '127.0.0.1'
port = 12345
name = ""

def send_message(string, sock):
	try:
		sock.sendall(name + ':' + string)
	except socket.error:
		print 'Send failed'
		sys.exit()


def setup_connection(host, port):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	except socket.error, msg:
		print 'Failed to create socket: ' + str(msg[1])
		sys.exit()
	# s.setblocking(0)
	try:
		remote_ip = socket.gethostbyname(host)
	except socket.gaierror:
		print 'Hostname could not be resolved. Exiting'
		sys.exit()


	s.connect((remote_ip, port))

	print 'Socket Conneted to ' + host + ' on ip ' + remote_ip
	return s


input = ""
# TODO get rid of message ready and add in Queue
message_ready = False
def get_input():
	global input, message_ready
	input = raw_input("> ")
	message_ready = True

name = raw_input("Please enter your chat name: ")

sock = setup_connection(host, port)

listener = threading._start_new_thread(get_input, ())

while True:
	# message = str(raw_input("Type something: "))
	# send_message(message, sock)
	if message_ready:
		# global input, message_ready
		listener = threading._start_new_thread(get_input, ())
		send_message(input, sock)
		input = ""
		message_ready = False
	receive = select.select([sock], [], [], 0.005)
	# Only check the rlist
	if receive[0]:
		message = sock.recv(4096)
		print message
import socket
from datetime import datetime
from json import dumps as stringToJSON

SOCKET_PATH = '/tmp/node-python-sock'

def generateTime():
	t = datetime.now()
	return '{}{}Z'.format(t.strftime('%Y-%m-%dT%H:%M:%S.'), t.strftime('%f')[0:3])

class comm():
	def __init__(self, path=None):
		self.numSent = 0
		self.sendHistory = []
		self.path = path if path else SOCKET_PATH
		self.client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
		self.client.connect(self.path)

	def send(self, data):
		msg = {'time': generateTime(),
			   'data': stringToJSON(data)}
		jsonMsg = stringToJSON(msg)
		self.client.send(jsonMsg.encode())
		self.sendHistory.append(msg)
		self.numSent += 1

	def close(self):
		self.client.close()
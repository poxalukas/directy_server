import rpyc
from constRPYC import * #-
from rpyc.utils.server import ThreadedServer

class Directory(rpyc.Service):
	registry={}

	def exposed_register(Self, server_name, ip_adress,port_number):
		self.registry[server_name] = (ip_adress, port_number)
		print(self.registry)
		return "Resgistration OK"

	def exposed_lookup(Self, server_name):
		print(self.registry)
		return self.registry[server_name]

if __name__ == "__main__":
	server = ThreadedServer(Directory,port = DIR_PORT)

server.start{}
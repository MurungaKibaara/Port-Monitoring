import socketserver

class MyTCPSocketHandler(socketserver.BaseRequestHandler):

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)

if __name__ == "__main__":
    
    HOST, PORT = "localhost", 9999

    server = socketserver.TCPServer((HOST, PORT), MyTCPSocketHandler)
    server.serve_forever()
    
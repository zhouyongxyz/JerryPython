import socketserver

class ComCoreHandler(socketserver.StreamRequestHandler):
    def handle(self):
        # self.rfile is a file-like object created by the handler;
        # we can now use e.g. readline() instead of raw recv() calls
        print("client is connected ip : " + self.client_address[0])
        # if self.controller:
        #     self.controller.clientHandlerList.append(self)
        #     self.controller.clientNameList.append(self.client_address[0])
        while True:
            self.data = self.rfile.readline().strip()
            if self.data != "":
                print("client : " + self.client_address[0] + "recv :" + str(self.data))
                # if self.callback:
                #     self.callback()
        # Likewise, self.wfile is a file-like object used to write back
        # to the client
        #self.wfile.write(self.data.upper())

    def setCallback(self,callback):
        print("register callback ...")
        self.callback = callback

    def setController(self,controller):
        self.controller = controller

    def sendMsg(self,msg):
        self.wfile.write(msg)



if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), ComCoreHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
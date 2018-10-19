import socket
import sys
import pickle
import threading

class Server:
    def __init__(self, host="localhost", port=3000):
        self.clients = []
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((str(host), int(port)))
        self.sock.listen(10)
        self.sock.setblocking(False)

        accept = threading.Thread(target=self.acceptConn)
        process = threading.Thread(target=self.processConn)

        accept.daemon = True
        accept.start()

        process.daemon = True
        process.start()

        while True:
            msg = input (">> ")
            if msg == "exit":
                self.sock.close()
                sys.exit()
            else:
                pass


    def acceptConn(self):
        print("Accepting connections")
        while True:
            try:
                conn, addr = self.sock.accept()
                conn.setblocking(False)
                self.clients.append(conn)
            except:
                pass

    def processConn(self):
        print("Processing connections")
        while True:
            if len(self.clients)>0:
                for c in self.clients:
                    try:
                        data = c.recv(1024)
                        if data:
                            self.msg_to_all(data, c)
                    except:
                        pass

    def msg_to_all(self, msg, client):
        for c in self.clients:
            try:
                if c != client:
                    c.send(msg)
            except:
                self.clients.remove(c)

s = Server()
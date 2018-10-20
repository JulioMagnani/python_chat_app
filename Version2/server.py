import socket
from messages import Greetings

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((host, port))

    s.listen(1)
    print("Waiting for client to connect")

    c, addr = s.accept()
    print(f"{str(addr)} is connected")

    while True:
        data = c.recv(1024).decode("utf-8")
        success_message = "Function run succesfully"
        failure_message = "Function failed to run"

        if not data:
            break
        elif data == 'h':
            Greetings.helloWorld()
            c.send(success_message.encode("utf-8"))
        elif data == 'g':
            Greetings.goodbeyeWorld()
            c.send(success_message.encode("utf-8"))
        else:  
            print("Not a valid function")
            c.send(failure_message.encode("utf-8"))
    
    c.close()

if __name__ == '__main__':
    Main()

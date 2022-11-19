import socket as Socket
# Represent the echo client


class Client:
    def __init__(self, ip_address, port_number, buffer_size):
        self.running = True
        self.socket = None
        self.ip_address = ip_address
        self.port_number = port_number
        self.buffer_size = buffer_size

    def start(self):
        """ 
        Attempts to acquire and conncet a socket at the specified address 
        and port, as well.  Will exit the program with an exception if the 
        socket is unsuccessfully acquired.
        """
        try:
            # AF_INET = designates the IPV4 protocol
            # SOCK_STREAM = designates the TCP protocol
            self.socket = Socket.socket(Socket.AF_INET, Socket.SOCK_STREAM)
            # Attempt
            self.socket.connect((self.ip_address, self.port_number))
        except:
            raise Exception(
                f"Failed to Initalize Socket({self.ip_address}, {self.port_number})")
        else:
            print("Socket acquired")

    def close(self):
        """ Closes the socket if it has been acquired."""
        if self.socket is not None:
            self.socket.close()

    def execute(self):
        """
        Assuming the client's socket has been established, block while  
        continually requesting user input, encode that data into utf-8 format, 
        transfer it over the wire, and await a response.  If the response 
        is exiting, will escape the function.
        """
        while self.running:
            message = input("Enter Message: ")
            if message == 'end':
                self.running = False
            self.socket.sendall(message.encode('utf-8'))
            reply = self.socket.recv(self.buffer_size)
            print(f"Received {reply.decode('utf-8')}")


if __name__ == "__main__":
    client = Client("127.0.0.1", 5000, 1024)
    client.start()
    client.execute()
    client.close()

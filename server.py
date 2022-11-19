import socket as Socket

class Server:
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
            self.socket = Socket.socket(Socket.AF_INET, Socket.SOCK_STREAM)
            # Ensures that the socket is closed if python crashes
            self.socket.setsockopt(Socket.SOL_SOCKET, Socket.SO_REUSEADDR, 1)
            # Set the listening address and port
            self.socket.bind((self.ip_address, self.port_number))
            # Marks the socket as passive, ie listener
            self.socket.listen()
        except:
            raise Exception(
                f"Failed to Initalize Socket({self.ip_address}, {self.port_number})")
        else:
            print("Socket acquired")

    def close(self):
        """ Closes the socket if it has been acquired."""
        if self.socket is not None:
            self.socket.close()

    def echo(self, connection):
        """
        Given a specific TCP connection, will receive data from the wire.
        If the data is invalid is not properly received will throw exception.
        Will decode the received data into a string, reverse the string, 
        reencode the data, and send it back out onto the wire.
        """
        incoming_data = connection.recv(self.buffer_size)
        if not incoming_data:
            raise Exception('Invalid Incoming Data')
        if (incoming_data == b'end'):
            self.running = False
        message = incoming_data.decode('utf-8')
        print(f"Received {message}")
        char_array = [*message]
        char_array.reverse()
        outgoing_data = str("").join(char_array).encode('utf-8')
        connection.sendall(outgoing_data)

    def execute(self):
        """
        Will await (blocking) the first connection, then will 
        continually service that connection until exit is requested. 
        """
        connection, address = self.socket.accept()
        print(f"Connected by {address}")
        while self.running:
            self.echo(connection)
        print(f"Closing connection {address}")
        connection.close()


if __name__ == "__main__":
    server = Server("127.0.0.1", 5000, 1024)
    server.start()
    server.execute()
    server.close()

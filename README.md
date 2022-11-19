The goal of this project was to explore the TCP protocol.
To this end, the python programming language and socket API were used in a simple and pedagogical manner. 
A socket is communications abstraction, that provides an interface for
managing and working with network protocols such as UDP and TCP.

The developed program provides two agents, the client and the server, 
both of whom communicate via a socket interface.  The client sends
messages to the server, who then processes the data.  The server 
performs string-reversal on the data, and then transmits it back 
over to the client. 

In this implementation, both the client and the server run on the user's
local machine, but this setup can be interfaced with any network connection.
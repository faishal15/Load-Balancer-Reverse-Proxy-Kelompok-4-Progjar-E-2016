import socket, sys, threading

#inisialisasi
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#proses binding
server_address = ('localhost', 8010)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

#listening
sock.listen(1)

counter = 1

def forwardedServer(messageToForward, link, port):
    forwardSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    linkAndPort = (link, port)
    forwardSocket.connect(linkAndPort)
    responData = ""
    try:
        #sending data
        message = messageToForward
        forwardSocket.sendall(message)
        
        #read data
        while True:
            dataServer = forwardSocket.recv(64)
            if dataServer:
                responData += dataServer
            else:
                break;
        print dataserver
    finally:
        return responData
        print "Closing socket"
        client_socket.close()
        #return responData

def forwardTo(conn, address, serverLink, serverPort):
    try:
        print >>sys.stderr, 'connection from ', address
        requestMessage = ""
        while True:
            data = conn.recv(64)
            data = bytes.decode(data)
            requestMessage += data
            if(requestMessage[-4:] == "\r\n\r\n"):
                break

        #forwarding the message

        backwardMessage = forwardedServer(requestMessage,serverLink, serverPort)
        conn.send(backwardMessage)
    finally:
        # Clean up the connection
        conn.close()

while True:
    #waiting for a connection
    print >>sys.stderr, 'waiting for a connection'
    clientConnection, clientIP = sock.accept()
    if (counter == 1):
        a = threading.Thread(target=forwardTo, args=(clientConnection,clientIP,'localhost',8011))
        a.start()
        counter+=1
    elif (counter == 2):
        b = threading.Thread(target=forwardTo, args=(clientConnection,clientIP,'localhost',8012))
        b.start()
        counter+=1
    elif (counter == 3):
        c = threading.Thread(target=forwardTo, args=(clientConnection,clientIP,'localhost',8013))
        c.start()
        counter+=1
    elif (counter == 4):
        d = threading.Thread(target=forwardTo, args=(clientConnection,clientIP,'localhost',8014))
        d.start()
        counter+=1
    elif (counter == 5):
        e = threading.Thread(target=forwardTo, args=(clientConnection,clientIP,'localhost',8015))
        e.start()
        counter+=1
    if(counter > 5):
        counter = 1

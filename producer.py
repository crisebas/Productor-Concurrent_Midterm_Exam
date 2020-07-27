def establish_connection(SOCKET, HOST, PORT):
    SOCKET.connect((HOST, PORT))

def declare_queue(SOCKET, action, queue_name):
    message_to_server = "DECLARE_QUEUE/" + action + "/" + queue_name + "\n"
    SOCKET.sendall(message_to_server.encode())

def send_message(SOCKET, message, queue_name):
    message_to_server = "MESSAGE/" + message + "/" + queue_name + "\n"
    SOCKET.sendall(message_to_server.encode())

def disconnect(SOCKET):
    SOCKET.sendall("DISCONNECT".encode())
    SOCKET.close()
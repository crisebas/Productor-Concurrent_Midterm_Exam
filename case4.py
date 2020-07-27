import socket
import producer as prod

def case4():
    HOST = "127.0.0.1"
    PORT = 3000
    SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    prod.establish_connection(SOCKET, HOST, PORT)

    action = "PUBLISH"
    request_queue = input("Enter queue name to declare: ")
    prod.declare_queue(SOCKET, action, request_queue)
    action = "SUBSCRIBE"
    reply_queue = "Reply_" + request_queue
    prod.declare_queue(SOCKET, action, reply_queue)

    message = input("Enter FIB N: ")
    prod.send_message(SOCKET, message, request_queue)
    
    reply = SOCKET.recv(1024)
    print(message + " = " + reply.decode())

    prod.disconnect(SOCKET)


case4()
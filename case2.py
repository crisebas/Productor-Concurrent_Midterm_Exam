import socket
import producer as prod

def case2():
    HOST = "127.0.0.1"
    PORT = 3000
    SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    prod.establish_connection(SOCKET, HOST, PORT)

    action = "PUBLISH"
    queue_name = input("Enter queue name to declare: ")
    prod.declare_queue(SOCKET, action, queue_name)

    message = input("Enter message: ")
    prod.send_message(SOCKET, message, queue_name)
    message = input("Enter message: ")
    prod.send_message(SOCKET, message, queue_name)
    message = input("Enter message: ")
    prod.send_message(SOCKET, message, queue_name)

    prod.disconnect(SOCKET)


case2()
import socket
import producer as prod

def case3():
    HOST = "127.0.0.1"
    PORT = 3000
    SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    prod.establish_connection(SOCKET, HOST, PORT)

    action = "PUBLISH"
    first_queue_name = input("Enter queue name to declare: ")
    prod.declare_queue(SOCKET, action, first_queue_name)
    second_queue_name = input("Enter queue name to declare: ")
    prod.declare_queue(SOCKET, action, second_queue_name)

    message = input("Enter message: ")
    prod.send_message(SOCKET, message, first_queue_name)
    prod.send_message(SOCKET, message, second_queue_name)
    message = input("Enter message: ")
    prod.send_message(SOCKET, message, first_queue_name)
    prod.send_message(SOCKET, message, second_queue_name)

    prod.disconnect(SOCKET)


case3()
import socket
import sys

#CREATE SOCKET FOR ESTABLISHING CONNECTION
def create_socket():
    try:
        global host
        global port
        global s
        host=""
        port=9999
        s=socket.socket()
    except socket.error as msg:
        print("SOCKET ERROR"+str(msg))

#BINDING SERVER AND PORT
def bind_socket():
    try:
        global host
        global port
        global s
        print("BINDING THE PORT " + str(port))
        s.bind((host,port))
        s.listen(5)
    except socket.error as msg:
        print("SOCKET BINDING ERROR "+str(msg)+"\n"+" RETRYING")
        bind_socket()

#ACCEPTING CONNECTION BY SERVER
def socket_accept():
    conn,address=s.accept()
    print("CONNECTION HAS BEEN ESTABLISHED! " + "IP"+address[0]+"| PORT"+str(address[1]))
    send_command(conn)
    conn.close()

#SENDING COMMAND TO LOCAL HOST
def send_command(conn):
    while True:
        cmd=input()
        if(cmd=='quit'):
            conn.close()
            socket.close
            sys.exit()
        if(len(str.encode(cmd))>0):
            conn.send(str.encode(cmd))
            client_response=str(conn.recv(1024),"utf-8")
            print(client_response,end=" ")

def main():
    create_socket()
    bind_socket()
    socket_accept()

main()
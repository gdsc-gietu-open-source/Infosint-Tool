import socket

def openport():
    ip = input("Enter ip address to get open ports:")
    for port in range(65535):
        try:
            serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            serv.bind((ip,port))
        except:
            print('[OPEN] Port open :',port)
        serv.close()

if __name__=="__main__":
   openport()
     
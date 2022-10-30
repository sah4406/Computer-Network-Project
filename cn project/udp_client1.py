import socket
from datetime import datetime
import colorama
from termcolor import colored
if __name__ == "__main__":
    # Here we define the UDP IP address as well as the port number that we have
    try:
        host="127.0.0.1"
        port =4455
        addr=(host,port)
    # SOCK_DGRAM for UDP packets
        client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    except socket.error as m:
        print("Socket not created, nor connected...Error:- " +str(m))
        exit()

    while True:
        # send data
        data=input("client(Enter City Name):")
        if data.lower()=="end":    
            break
        data = data.encode("utf-8")
        client.sendto(data,addr) 
        # Receive the client packet along with the address it is coming from
        data,addr=client.recvfrom(1024)
        data = data.decode("utf-8")
        if(data=="City not Found!!"):
            print(data)
        else:
            data=data.split()
            deg_cel=float(data[0])
            deg_cel="{:.2f}".format(deg_cel)
            deg_cel=deg_cel+"°C"
            pressure=data[1]+"mbar"
            description=data[2]
            colorama.init()
            print(colored("Tempertaure :",'yellow'),colored(deg_cel,'green'))
            print(colored("pressure    :",'yellow'),colored(pressure,'green'))
            print(colored("Description :",'yellow'),colored(description,'green'))
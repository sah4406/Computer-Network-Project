import json
import socket
import requests
if __name__ == "__main__":
    try:
        host="127.0.0.1"
        port=4455
        # Create a UDP socket
        server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        print("Socket created.....")
    except socket.error as m1:
        print("Socket could not be created....ERROR:- " +str(m1))
        exit()

    try:
        server.bind((host,port))
        print("Socket binded...")
    except socket.error as m2:
        print("->socket could not bind.... ERROR:- " +str(m2))
    while True:
        # received
        data,addr = server.recvfrom(1024)
        # decoding in utf-8
        data = data.decode("utf-8")
        # Api to fetch weather data
        complete_url="https://api.openweathermap.org/data/2.5/weather?q="+data+"&appid=71f5bf449a40505943bb2ff2d6350269"
        response = requests.get(complete_url)
        x=response.json()
        if x["cod"]==200:
             y=x["main"]
             temp=str(y["temp"]-273.15)
             press=str(y["pressure"])
             z=x["weather"]
             weather_descp=str(z[0]["description"])
             x=temp+" "+press+" "+weather_descp
             user_encode_data = x.encode('utf-8')
             server.sendto(user_encode_data,addr)
             print("Weather Data send")
        else:
             msg="City not Found!!"
             msg=msg.encode('utf-8')
             server.sendto(msg,addr)
             print("No Data Found!!")
        
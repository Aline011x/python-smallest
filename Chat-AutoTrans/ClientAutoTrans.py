import socket


lang = input("Please enter your lenguage: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 4444))

while True: 
    message = input("")
    if message == "!q":
        client.close()
        break
    
    else: 
        client.send(f"[{lang}]{message}".encode())
    

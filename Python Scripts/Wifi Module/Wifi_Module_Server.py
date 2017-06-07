'''
Author: Mason Edgar
Supervisor: John Sochacki

SERVER SIDE PYTHON SCRIPT

'''


import socket 



def Main():
    
    host_name_string = socket.gethostname()
    
    host_ip = socket.gethostbyname(host_name_string)
    
    port = 5555
    
    s = socket.socket()
    
    s.bind((host_ip, port))
    
    print("\nWaiting on client....")
    
    s.listen(1)
    
    client, clientAddress = s.accept()
    
    print("Connection from: " + str(clientAddress))
    
    while True: 
        data = client.recv(1024).decode('utf-8')
        if not data:
            break
        print("Data entered from client: " + data)
        data = data.upper()
        print("Sending this back to client: " + data)
        client.send(data.encode('utf-8'))
    
    client.close()
    
#    print(host_name_string)
#    print(host_ip)
    
    
if __name__ == '__main__':
    Main()
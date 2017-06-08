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
    
    print("\nConnection from: " + str(clientAddress))
    
    print("\nHex Values In Descending Order:\n")
    
    temp1 = client.recv(1024).decode('utf-8')
    
    temp2 = client.recv(1024).decode('utf-8')

    temp1_str  = str(temp1)
    
    temp3 = str(temp2)
    
    temp4 = temp3.split(' ')
       
    temp4.insert(0, temp1_str)
    
    hex_values = temp4[0].split(' ')
    
    
    for x in range(0,13):
        print(hex_values[x])


    client.close()
    
    
if __name__ == '__main__':
    Main()
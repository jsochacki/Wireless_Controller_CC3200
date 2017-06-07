import socket 

def Main():
    
#    host_name_string = socket.gethostname()
    
#    host_ip = socket.gethostbyname(host_name_string)

    host_ip = '172.27.194.123'
    
    port = 5555
    
#    print(host_ip)
    
    s = socket.socket()
    
    s.connect((host_ip, port))

    user_message = input("Enter text here: ")
    
    while user_message != "quit": 
        s.send(user_message.encode('utf-8'))
        data = s.recv(1024).decode('utf-8')
        print("Message recieved from server: " + data)
        user_message = input("Enter text here: ")
        
        
    s.close()
    

    
if __name__ == '__main__':
    Main()
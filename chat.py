

message="""
    input 1 for send task
    input 2 for receiving task
    """
while True:
        print(message)
        
        input_value=int(input("plz enter the number"))


        if input_value==1:
            import socket
            s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
            # target_ip="192.168.239.249"
            target_ip="127.0.0.1"
            port_no=2525
            target_address=(target_ip,port_no)




            message=input("write your message:")

            encrypt_message=message.encode("ascii")
            s.sendto(encrypt_message,target_address)

            # __________________________________________________________________
            
                # ___________________________________________________________________________________

        elif input_value==2:
            import socket
            s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            # ip_address ="192.168.239.249"
            ip_address="127.0.0.1"
# ip_address="127.0.0.1" # this is for someone who is present anywhere
            port_no =2525 #this is for upflaire for multiple person
            complete_address=(ip_address,port_no)
            s.bind(complete_address)
            print("hey i am receiving your message")

            message =s.recvfrom(100)
            print(message)
            sender_address=message[1][0]
            received_message=message[0]
            decrypted_message =received_message.decode("ascii")
            print(decrypted_message)
            with open(sender_address+".txt",'a+')as file:
                file.write(decrypted_message +'\n')
        
   
        
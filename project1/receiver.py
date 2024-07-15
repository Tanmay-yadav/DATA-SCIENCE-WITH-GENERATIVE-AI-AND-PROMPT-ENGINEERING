import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_address ="192.168.1.73"
# ip_address="127.0.0.1" # this is for someone who is present anywhere
port_no =2525 #this is for upflaire for multiple person
complete_address=(ip_address,port_no)
s.bind(complete_address)

print("hey i am receiving your message")
while True:
    message =s.recvfrom(100)
    print(message)
    sender_address=message[1][0]
    received_message=message[0]
    decrypted_message =received_message.decode("ascii")
    print(decrypted_message)
    with open(sender_address+".txt",'a+')as file:
        file.write(decrypted_message +'\n')
    



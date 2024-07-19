import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

target_ip="192.168.239.224"
port_no=2525
target_address=(target_ip,port_no)



condition =True
while condition:
    message=input("write your message:")
    # for i in range(10):
        # message= "hello"
        # print(message)
    encrypt_message=message.encode("ascii")
    s.sendto(encrypt_message,target_address)

    # ______________________homework____________________
    # ........................research and work...............................
    # receiver will send "received " to the sender after getting message
    # how to send file,photo,docx,etc
    # message+time+date
    # ...................................................................
import socket
from datetime import datetime

message = """
    input 1 for send task
    input 2 for receiving task
    """

while True:
    print(message)
    input_value = int(input("plz enter the number"))

    if input_value == 1:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # target_ip = "192.168.239.249"
        target_ip = "127.0.0.1"
        port_no = 5500
        target_address = (target_ip, port_no)

        message = input("write your message: ")

        encrypt_message = message.encode("ascii")
        s.sendto(encrypt_message, target_address)

    elif input_value == 2:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # ip_address = "192.168.239.249"
        ip_address = "127.0.0.1"
        port_no = 5500
        complete_address = (ip_address, port_no)
        s.bind(complete_address)
        print("hey I am receiving your message")

        message = s.recvfrom(100)
        sender_address = message[1][0]
        received_message = message[0]
        decrypted_message = received_message.decode("ascii")
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        print(f"Message received at {current_time}: {decrypted_message}")
        
        with open(sender_address + ".txt", 'a+') as file:
            file.write(f"{current_time} - {decrypted_message}\n")

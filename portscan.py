import socket
#coding=utf-8
host = input("URL/IP: ")
ports=[21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 3306, 3389, 8080]
for port in ports:
    client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.03)
    r = client.connect_ex((host, port))
    if r == 0:
        print(str(port)+(" ◄ Open"))
    else:
        print(str(port)+(" • Closed"))
print("Scan accomplished\n")

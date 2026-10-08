import socket

target = "127.0.0.1"
ports_to_check = [22, 80, 443, 5000, 8080]

for port in ports_to_check:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target, port))

    if result == 0:
        print(f"Port {port}: OPEN")
    else:
        print(f"Port {port}: closed")

    s.close()
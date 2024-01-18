import sys
import socket
import time
import random
from concurrent.futures import ThreadPoolExecutor

SOCKET_TIMEOUT = 1.5  # seconds
MAX_THREADS = 32
RETRY_COUNT = 1

def check_host_port(host, port, retries=RETRY_COUNT):
    for _ in range(retries):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(SOCKET_TIMEOUT)
                s.connect((host, port))
            return True
        except:
            pass
    return False

def parse_ports(ports):
    result = set()
    for part in ports.split(","):
        if "-" in part:
            start, end = map(int, part.split("-"))
            result.update(range(start, end + 1))
        else:
            result.add(int(part))
    return list(result)

def scan_ports_threaded(host, ports):
    random.shuffle(ports)  # randomize port order
    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        results = executor.map(lambda port: (port, check_host_port(host, port)), ports)
    return [port for port, isOpen in results if isOpen]

def main():
    if len(sys.argv) != 3:
        print("Usage: python basic_port_scanner.py <host> <port>")
        sys.exit(1)

    i_host, i_ports = sys.argv[1], sys.argv[2]
    ports = parse_ports(i_ports)

    print(f"Scanning host: {i_host}")

    start_time = time.time()
    open_ports = scan_ports_threaded(i_host, ports)
    elapsed_time = time.time() - start_time

    if open_ports:
        print("Open ports:")
        print(sorted(open_ports))
    else:
        print("No open ports found.")

    print(f"Elapsed time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    main()

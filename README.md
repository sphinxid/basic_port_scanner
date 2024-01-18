# Basic Port Scanner

A simple, multi-threaded port scanner written in Python. It's designed to scan a range of ports on a given host to identify open ports. This tool is useful for network administrators and security professionals to audit networked services.

## Features

- **Multi-threaded scanning:** Utilizes threading for faster performance.
- **Socket Timeout Adjustment:** Customizable timeout for network connections.
- **Retry Mechanism:** Retries scanning a port if the initial attempt fails, enhancing reliability.
- **Randomized Scan Order:** Scans ports in a randomized order to reduce the likelihood of detection by simple rate-limiting defenses.

## Requirements

- Python 3.x

## Usage

To use the port scanner, run the script from the command line with the host and port range as arguments.

python basic_port_scanner.py <host> <port range>

- `<host>`: The target hostname or IP address.
- `<port range>`: The range of ports to scan, e.g., `80,443,1000-2000`.

### Example

python basic_port_scanner.py 192.168.1.1 80,443,1000-2000

## Configuration

You can modify the following settings in the script to suit your needs:

- `SOCKET_TIMEOUT`: Duration (in seconds) before a socket connection times out.
- `MAX_THREADS`: Maximum number of threads for parallel scanning.
- `RETRY_COUNT`: Number of retries for each port.

## Disclaimer

This tool is intended for educational and legitimate network auditing purposes only. Unauthorized scanning and/or breaking into networks without explicit permission is illegal. The author is not responsible for misuse or damage caused by this program.


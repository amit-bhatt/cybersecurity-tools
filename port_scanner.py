import socket
import sys

def scan_ports(target):
    print(f"[+] Scanning target: {target}")
    for port in range(1, 1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        try:
            s.connect((target, port))
            print(f"[+] Port {port} is open")
        except:
            pass
        finally:
            s.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python port_scanner.py <target_ip>")
        sys.exit(1)

    target_ip = sys.argv[1]
    scan_ports(target_ip)

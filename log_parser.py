import re
import sys

def parse_auth_log(file_path):
    failed_login_pattern = r"Failed password for(?: invalid user)? (\w+) from ([\d.]+)"
    
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.readlines()
    except FileNotFoundError:
        print(f"[-] File not found: {file_path}")
        return

    print("[+] Failed SSH login attempts:")
    for line in content:
        match = re.search(failed_login_pattern, line)
        if match:
            username, ip = match.groups()
            print(f"User: {username}, IP: {ip}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python log_parser.py <path_to_auth_log>")
        sys.exit(1)

    log_file = sys.argv[1]
    parse_auth_log(log_file)

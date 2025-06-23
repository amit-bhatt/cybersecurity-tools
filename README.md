# 🛡️ Cybersecurity Tools

A collection of Python-based cybersecurity and ethical hacking tools for automating common tasks such as port scanning, password generation, log parsing, and hash cracking.

---

## 📂 Tools Included

### 🔍 1. `port_scanner.py`
A simple TCP port scanner that checks for open ports on a target host.

**Usage:**
```bash
python port_scanner.py 192.168.1.1
```

### 🔍 2. `password_generator.py`
This script generates secure random passwords with a mix of letters, digits, and symbols.

**Usage:**
```bash
python password_generator.py 16
```

### 🔍 3. `log_parser.py`
This script parses Linux authentication logs (like /var/log/auth.log) to extract failed SSH login attempts — useful for log monitoring and brute-force detection.

**Usage:**
```bash
python log_parser.py /var/log/auth.log
```
### 🔍 4. `hash_cracker.py`
This script cracks MD5, SHA1, or SHA256 hashes using a dictionary attack. You provide:
    1. A file with hashes (one per line)
    2. A wordlist (dictionary file)
    3. Hash type

**Usage:**
```bash
python hash_cracker.py hashes.txt wordlist.txt md5
```


import hashlib
import sys

def load_hashes(file_path):
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"[-] Hash file not found: {file_path}")
        sys.exit(1)

def load_wordlist(wordlist_path):
    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"[-] Wordlist not found: {wordlist_path}")
        sys.exit(1)

def hash_word(word, hash_type):
    h = hashlib.new(hash_type)
    h.update(word.encode())
    return h.hexdigest()

def crack_hashes(hashes, wordlist, hash_type):
    print(f"[+] Cracking {len(hashes)} hashes using {hash_type.upper()} and wordlist of {len(wordlist)} words...\n")
    for target_hash in hashes:
        found = False
        for word in wordlist:
            if hash_word(word, hash_type) == target_hash:
                print(f"[+] Hash cracked: {target_hash} => {word}")
                found = True
                break
        if not found:
            print(f"[-] Not found: {target_hash}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python hash_cracker.py <hash_file> <wordlist_file> <hash_type>")
        print("Example: python hash_cracker.py hashes.txt rockyou.txt md5")
        sys.exit(1)

    hash_file = sys.argv[1]
    wordlist_file = sys.argv[2]
    hash_type = sys.argv[3].lower()

    if hash_type not in ['md5', 'sha1', 'sha256']:
        print("[-] Supported hash types: md5, sha1, sha256")
        sys.exit(1)

    hashes = load_hashes(hash_file)
    wordlist = load_wordlist(wordlist_file)

    crack_hashes(hashes, wordlist, hash_type)

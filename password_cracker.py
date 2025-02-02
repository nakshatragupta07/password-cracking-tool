import argparse  
import string  
import itertools  
import time  

def brute_force(password, max_length=8):  
    chars = string.ascii_letters + string.digits + string.punctuation  
    for length in range(1, max_length + 1):  
        for attempt in itertools.product(chars, repeat=length):  
            attempt = ''.join(attempt)  
            if attempt == password:  
                return attempt  
    return None  

def dictionary_attack(password, wordlist_path="wordlist.txt"):  
    try:  
        with open(wordlist_path, "r", encoding="utf-8") as file:  
            for word in file:  
                word = word.strip()  
                if word == password:  
                    return word  
        return None  
    except FileNotFoundError:  
        return "Wordlist file not found!"  

def password_strength(password):  
    strength = 0  
    if len(password) >= 8:  
        strength += 1  
    if any(char.isdigit() for char in password):  
        strength += 1  
    if any(char.isupper() for char in password):  
        strength += 1  
    if any(char in string.punctuation for char in password):  
        strength += 1  
    return strength  

def pci_compliance_check(password):  
    if len(password) < 7:  
        return False  
    if not any(char.isdigit() for char in password):  
        return False  
    if not any(char.isupper() for char in password):  
        return False  
    if not any(char in string.punctuation for char in password):  
        return False  
    return True  

def main():  
    parser = argparse.ArgumentParser(description="Password Cracking Tool")  
    parser.add_argument("password", help="Password to crack or check")  
    parser.add_argument("--brute-force", action="store_true", help="Use brute force attack")  
    parser.add_argument("--dictionary", action="store_true", help="Use dictionary attack")  
    parser.add_argument("--check-strength", action="store_true", help="Check password strength")  
    parser.add_argument("--pci-check", action="store_true", help="Check PCI compliance")  
    args = parser.parse_args()  

    if args.brute_force:  
        print("\n[+] Starting Brute Force Attack...")  
        start_time = time.time()  
        result = brute_force(args.password)  
        end_time = time.time()  
        print(f"Brute Force Attack Result: {result}")  
        print(f"Time Taken: {end_time - start_time:.2f} seconds")  

    if args.dictionary:  
        print("\n[+] Starting Dictionary Attack...")  
        start_time = time.time()  
        result = dictionary_attack(args.password)  
        end_time = time.time()  
        print(f"Dictionary Attack Result: {result}")  
        print(f"Time Taken: {end_time - start_time:.2f} seconds")  

    if args.check_strength:  
        print("\n[+] Checking Password Strength...")  
        strength = password_strength(args.password)  
        print(f"Password Strength: {strength}/4")  

    if args.pci_check:  
        print("\n[+] Checking PCI Compliance...")  
        compliance = pci_compliance_check(args.password)  
        print(f"PCI Compliance: {compliance}")  

if __name__ == "__main__":  
    main()  
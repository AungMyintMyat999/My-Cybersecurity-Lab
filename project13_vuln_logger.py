import socket

# STEP 1: Simple Database (Mapping versions to known risks)
vuln_db = {
    "OpenSSH_6.6.1p1": "User Enumeration & Remote Code Execution (RCE)",
    "Apache/2.4.7": "Heartbleed vulnerability (depending on OpenSSL version)",
    "Nginx/1.6.2": "Buffer Overflow vulnerability"
}


# STEP 2: The Scanner & Matcher Logic
def check_vulnerability(banner):
    found = False
    for version, risk in vuln_db.items():
        if version in banner:
            print(f"\n[!!!] CRITICAL: Known Vulnerability Found!")
            print(f"[!] Software: {version}")
            print(f"[!] Risk: {risk}")
            found = True

    if not found:
        print("\n[+] No common vulnerabilities found in local database for this banner.")


# ── STEP 3: Banner Grabbing Part ──
def get_banner(ip, port):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((ip, port))

        # Simple HTTP request for web ports
        if port == 80:
            s.send(b"GET / HTTP/1.1\r\nHost: " + ip.encode() + b"\r\n\r\n")

        banner = s.recv(1024).decode(errors='ignore').strip()
        return banner
    except Exception as e:
        return f"Error: {e}"


# ── STEP 4: Execution ──
target = input("Enter Target (e.g., scanme.nmap.org): ")  # Read Target
port = int(input("Enter Port: "))  # Read Port

print(f"\n[~] Scanning {target}:{port}...")
banner_result = get_banner(target, port)

print(f"[+] Banner Captured: {banner_result}")

# Check the captured banner against our database
check_vulnerability(banner_result)
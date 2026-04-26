import socket

# ── STEP 1: Variables (User Configuration) ──
target = input("Enter Target IP/Domain: ")  # Read Target
port = int(input("Enter Port to check (e.g., 21, 22, 80): "))  # Read Port


# ── STEP 2: The Banner Grabbing Logic ──
def get_banner(ip, port):
    try:
        s = socket.socket()  # Create socket object
        s.settimeout(2)
        s.connect((ip, port))  # Connect to the target machine

        # We try to receive the "Banner" (Service identification string)
        banner = s.recv(1024).decode().strip()  # Read Service info
        return banner
    except Exception as e:
        return f"Could not get banner: {e}"


# ── STEP 3: Execution ──
print(f"\n[!] Project 12: Grabbing banner from {target}:{port}...")
service_info = get_banner(target, port)

print(f"\n[+] Service Information: {service_info}")
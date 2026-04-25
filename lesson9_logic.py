# ── STEP 1: Inputs ──
# Get target info from user
target_ip = input("Target IP: ")
port_num = int(input("Enter a port to check (e.g., 21, 22, 80, 443): "))

# ── STEP 2: Decision Logic ──
def identify_service(ip, port):
    print(f"\n[*] Investigating {ip} on Port {port}...")
    
    # Using If-Elif-Else to classify the port
    if port == 21:
        service = "FTP (File Transfer Protocol) - Often has weak security"
    elif port == 22:
        service = "SSH (Secure Shell) - Used for remote access"
    elif port == 80:
        service = "HTTP (Web Server) - Unencrypted traffic"
    elif port == 443:
        service = "HTTPS (Secure Web) - Encrypted traffic"
    else:
        service = "Unknown Service - Manual analysis required"
        
    print(f"[!] Result: Found {service}")

# ── STEP 3: Execution ──
# Call the function with user input
identify_service(target_ip, port_num)
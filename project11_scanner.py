import socket

# ── STEP 1: Variables (User Configuration) ──
target = input("Target IP/Domain: ") # Read Target
start_p = int(input("Start Port: "))  # Starting point
end_p = int(input("End Port: "))      # Ending point

print(f"\n[!] Project 11: Launching scan on {target}...")

# ── STEP 2: Scanning Logic ──
def start_scan(ip, start, end):
    for port in range(start, end + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5) 
        
        result = s.connect_ex((ip, port))
        
        if result == 0:
            print(f"[+] Port {port}: OPEN")
        
        s.close() 

# ── STEP 3: Execution ──
start_scan(target, start_p, end_p)
print("\n[+] Scanning Mission Accomplished.")
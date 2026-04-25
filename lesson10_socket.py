import socket # STEP 1: Import the network library

# STEP 2: Setup Target
target_ip = input("Enter a target (e.g., scanme.nmap.org): ")
port_to_test = int(input("Enter port to test (try 80): "))

# STEP 3: Network Connection Logic
def check_port(ip, port):
    # Create a socket object (IPv4, TCP connection)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Set a timeout (Wait only 3 seconds)
    s.settimeout(3)
    
    print(f"[*] Attempting to connect to {ip} on port {port}...")
    
    # Try to connect (connect_ex returns 0 if success)
    result = s.connect_ex((ip, port))
    
    # STEP 4: Analyze Result
    if result == 0:
        print(f"[+] Port {port} is OPEN!")
    else:
        print(f"[-] Port {port} is CLOSED or unreachable.")
    
    # Close the connection
    s.close()

# STEP 5: Execution
check_port(target_ip, port_to_test)
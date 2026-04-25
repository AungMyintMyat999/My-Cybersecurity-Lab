# STEP 1: Variables (Collect inputs from user)
# Read Target IP
target_ip = input("Enter target IP address: ")

# Read Port Number and convert to integer
# We use int() to change text into a number
port_count = int(input("How many ports should I scan?: "))

# STEP 2: Function Logic
def start_interactive_scan(ip, limit):
    print(f"\n[*] Starting security audit on {ip}...")
    
    # Loop to repeat scanning based on user input
    for port in range(1, limit + 1):
        # Print status for each port
        print(f"Scanning Port {port}: [ANALYZING]")
    
    print(f"\n[+] Audit for {ip} is 100% complete.")

# STEP 3: Execution
# Run the function with our variables
start_interactive_scan(target_ip, port_count)
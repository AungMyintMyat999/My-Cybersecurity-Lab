#  STEP 1: Define the Function
def start_port_scanner(ip_address, max_ports):
    # This function takes an IP and a number of ports as input
    print(f"--- Starting Security Audit for {ip_address} ---")
    
    for port in range(1, max_ports + 1):
        print(f"Port {port}: Checking vulnerability...")
    
    print(f"--- Audit Finished for {ip_address} ---")

#  STEP 2: Use (Call) the Function 
target_1 = "10.0.0.1"
target_2 = "172.16.0.5"

start_port_scanner(target_1, 3) 
print("\n") 
start_port_scanner(target_2, 2)

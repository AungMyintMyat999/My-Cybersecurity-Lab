#  STEP 1: Setup Variables ──
target_ip = "192.168.1.1"
total_ports = 5

#  STEP 2: The Loop (Automation) ──
print(f"Starting Scan on {target_ip}...")

for port_number in range(1, total_ports + 1):
    # This block repeats for each port
    print(f"Checking Port: {port_number} - Status: SCANNING")

#  STEP 3: Final Output ──
print("Scan Task Completed Successfully.")

import socket
import threading
from queue import Queue

# ── STEP 1: Configuration ──
# We define a list of targets (In Phase 2, we will automate this range)
targets = ["scanme.nmap.org", "google.com", "bing.com"]
ports = [21, 22, 80, 443]  # Common ports to check


# ── STEP 2: The Core Scanning Function ──
def scan_target(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((ip, port))

        if result == 0:
            # If port is open, try to get a quick banner
            try:
                if port == 80:
                    s.send(b"GET / HTTP/1.1\r\nHost: " + ip.encode() + b"\r\n\r\n")
                banner = s.recv(1024).decode(errors='ignore').split('\n')[0].strip()
            except:
                banner = "No banner available"

            print(f"[+] {ip}:{port} is OPEN | Banner: {banner}")
        s.close()
    except:
        pass


# ── STEP 3: The Orchestrator (The Boss) ──
def orchestrator():
    print(f"--- Launching Multi-Target Scan ---")
    threads = []

    for target in targets:
        print(f"\n[*] Starting scan on: {target}")
        for port in ports:
            # Creating a thread for each target-port combination
            t = threading.Thread(target=scan_target, args=(target, port))
            threads.append(t)
            t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()
    print(f"\n--- All Scans Completed ---")


# ── STEP 4: Execution ──
if __name__ == "__main__":
    orchestrator()
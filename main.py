import sys
import os

# Ensure the 'src' directory is in the Python module search path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from sniffer import start_sniffer

def main():
    print("=" * 60)
    print("       JA4-PROBE: TLS HANDSHAKE ANALYZER & SNIFFER")
    print("       CodeAlpha Cybersecurity Internship - Task 1")
    print("=" * 60)
    print("[*] Initializing packet capture engine...")
    print("[*] Target Filter: TCP Port 443 (HTTPS/TLS traffic)")
    print("[*] Logs will be automatically saved to: logs/capture_log.json")
    print("-" * 60)
    
    try:
        # Run sniffer for 35 packets by default
        start_sniffer(count=35)
    except KeyboardInterrupt:
        print("\n[-] Sniffer session manually stopped by user.")
    except Exception as e:
        print(f"\n[!] An error occurred during execution: {e}")

if __name__ == "__main__":
    main()
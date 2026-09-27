from scapy.all import sniff, TCP, IP
from parser import parse_tls_client_hello
from logger import save_log_entry

def packet_callback(packet):
    """
    Callback function executed for every captured packet.
    """
    if packet.haslayer(IP) and packet.haslayer(TCP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport
        
        # Pass packet to our TLS parser
        tls_info = parse_tls_client_hello(packet)
        
        if tls_info and tls_info.get("is_client_hello"):
            print(f"[+] TLS ClientHello Found! 🚀 | {src_ip}:{src_port} --> {dst_ip}:{dst_port} | Version: {tls_info['tls_version']} | Size: {tls_info['payload_length']} bytes")
            
            # Save structured log entry to logs/capture_log.json
            save_log_entry(
                src=f"{src_ip}:{src_port}",
                dst=f"{dst_ip}:{dst_port}",
                version=tls_info['tls_version'],
                size=tls_info['payload_length']
            )
        else:
            print(f"[-] TCP Packet (Handshake/Ack): {src_ip}:{src_port} --> {dst_ip}:{dst_port}")

def start_sniffer(count=30):
    """
    Starts the Scapy sniffer targeting port 443 (HTTPS/TLS).
    """
    print("[*] Starting JA4-Probe Packet Sniffer...")
    print("[*] Listening for HTTPS (port 443) traffic. Please browse an HTTPS website now!")
    
    sniff(
        filter="tcp port 443",
        prn=packet_callback,
        count=count,
        store=False
    )
    print("[*] Capture session completed. Check logs/capture_log.json for saved output!")

if __name__ == "__main__":
    start_sniffer(count=30)
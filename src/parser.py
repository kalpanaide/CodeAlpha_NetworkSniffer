from scapy.all import TCP, Raw

def parse_tls_client_hello(packet):
    """
    Inspects a TCP packet payload to check if it contains a TLS ClientHello handshake.
    Returns a dictionary of extracted metadata if found, otherwise None.
    """
    # Check if the packet has a TCP payload layer
    if packet.haslayer(TCP) and packet.haslayer(Raw):
        payload = bytes(packet[Raw].load)
        
        # TLS Record Header format:
        # Byte 0: Content Type (22 = Handshake)
        # Bytes 1-2: TLS Version (e.g., 0x0303 for TLS 1.2 / ClientHello compatibility)
        # Bytes 3-4: Length of record
        if len(payload) > 5 and payload[0] == 22:
            tls_content_type = payload[0]
            tls_version_major = payload[1]
            tls_version_minor = payload[2]
            
            # Byte 5: Handshake Type (1 = ClientHello)
            handshake_type = payload[5]
            
            if handshake_type == 1:
                return {
                    "is_client_hello": True,
                    "content_type": tls_content_type,
                    "tls_version": f"0x{tls_version_major:02x}{tls_version_minor:02x}",
                    "payload_length": len(payload)
                }
                
    return {"is_client_hello": False}
from scapy.all import sniff, IP, TCP, UDP

def packet_callback(packet):
    # Example: Print packet summary
    print(packet.summary())
    
    # Optional: Dive deeper, e.g., check for IP layer
    if IP in packet:
        src = packet[IP].src
        dst = packet[IP].dst
        print(f"IP Packet: {src} -> {dst}")
        
    # Check for TCP or UDP
    if TCP in packet:
        print(f"TCP Port: {packet[TCP].sport} -> {packet[TCP].dport}")
    elif UDP in packet:
        print(f"UDP Port: {packet[UDP].sport} -> {packet[UDP].dport}")



sniff(prn=packet_callback, filter="ip", store=False)  # store=False to avoid memory buildup

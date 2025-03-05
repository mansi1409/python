from scapy.all import sniff, IP, TCP, UDP, Raw

def packet_callback(packet):
    # Check if the packet has an IP layer
    if IP in packet:
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        protocol = ip_layer.proto
        
        # Print relevant information
        print(f"Source IP: {src_ip}, Destination IP: {dst_ip}, Protocol: {protocol}")
        
        # Check for TCP or UDP and print payload if available
        if TCP in packet:
            print(f"TCP Payload: {bytes(packet[TCP].payload)}")
        elif UDP in packet:
            print(f"UDP Payload: {bytes(packet[UDP].payload)}")
        elif Raw in packet:
            print(f"Raw Payload: {bytes(packet[Raw].load)}")
        
        print("-" * 50)

def main():
    print("Starting packet sniffer...")
    # Start sniffing packets
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    main()
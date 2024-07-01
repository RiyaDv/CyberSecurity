from scapy.all import *

# File to save packet records
log_file = "packet_logs.txt"

def packet_callback(packet):
    with open(log_file, "a") as f:
        if IP in packet:
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            protocol = packet[IP].proto

            f.write(f"IP Packet: {src_ip} -> {dst_ip} Protocol: {protocol}\n")

            if TCP in packet:
                src_port = packet[TCP].sport
                dst_port = packet[TCP].dport
                f.write(f"TCP Port: {src_port} -> {dst_port}\n")

                if packet.haslayer(Raw):
                    f.write(f"Raw Data: {packet[Raw].load}\n")
            
            elif UDP in packet:
                src_port = packet[UDP].sport
                dst_port = packet[UDP].dport
                f.write(f"UDP Port: {src_port} -> {dst_port}\n")

                if packet.haslayer(Raw):
                    f.write(f"Raw Data: {packet[Raw].load}\n")

            f.write("-" * 50 + "\n")

# Print a start message
print("Packet sniffer started. Capturing packets...")

# Use conf.L3socket to sniff packets at layer 3 (IP layer)
sniff(prn=packet_callback, store=0, filter="ip")

# Print a stop message
print("\nPacket sniffer stopped.")

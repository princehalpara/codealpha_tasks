from scapy.all import sniff, IP, TCP, UDP, ICMP

def packet_callback(packet):
    print("\n---------------- Packet Captured ----------------")

    if packet.haslayer(IP):
        source_ip = packet[IP].src
        destination_ip = packet[IP].dst
        protocol = packet[IP].proto

        print("Source IP      :", source_ip)
        print("Destination IP :", destination_ip)

        if packet.haslayer(TCP):
            print("Protocol       : TCP")
            print("Source Port    :", packet[TCP].sport)
            print("Destination Port:", packet[TCP].dport)

        elif packet.haslayer(UDP):
            print("Protocol       : UDP")
            print("Source Port    :", packet[UDP].sport)
            print("Destination Port:", packet[UDP].dport)

        elif packet.haslayer(ICMP):
            print("Protocol       : ICMP")

        else:
            print("Protocol Number:", protocol)

        if packet.payload:
            print("Packet Summary :", packet.summary())

    else:
        print("Non-IP Packet Captured")
        print(packet.summary())


print("Basic Network Sniffer Started...")
print("Capturing 10 packets...\n")

sniff(prn=packet_callback, count=10)

print("\nPacket Capturing Completed.")
from scapy.all import TCP, IP, send, sr1

def main():
    syn_segment = IP(dst = 'www.google.com')/TCP(sport = 10000, dport = 80, seq = 123, flags = 2)
    syn_segment.show()
    
    syn_ack_packet = sr1(syn_segment)
    syn_ack_packet.show()
    next = syn_ack_packet[TCP].seq + 1
    
    ack_segment = IP(dst = 'www.google.com')/TCP(sport = 10000, dport = 80, seq = syn_ack_packet[TCP].ack, ack = next, flags = 16)
    ack_segment.show()
    send(ack_segment)
         
if __name__ == "__main__":
    main()
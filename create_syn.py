from scapy.all import TCP

def main():
    syn_segment = TCP(dport=80, seq=123, flags= 2)
    syn_segment.show()

if __name__ == "__main__":
    main()
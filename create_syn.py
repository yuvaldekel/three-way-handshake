from scapy.all import TCP

def main():
    syn_segment = TCP()
    syn_segment.show()

if __name__ == "__main__":
    main()
import socket
import struct

def parse_ip_header(packet):
    """Analizza l'header IP per ottenere gli indirizzi mittente e destinatario."""
    ip_header = packet[:20]  # I primi 20 byte rappresentano l'header IP
    unpacked = struct.unpack("!BBHHHBBH4s4s", ip_header)
        #!: Usa il network byte order (Big Endian).
        # BB: Versione del protocollo e lunghezza dell'header.
        # HHH: Lunghezza totale del pacchetto, identificatore e flag/offset.
        # BB: Time To Live (TTL) e protocollo.
        # H: Checksum dell'header.
        # 4s: IP sorgente in forma binaria (4 byte).
        # 4s: IP destinazione in forma binaria (4 byte).


    src_ip = socket.inet_ntoa(unpacked[8])  # Indirizzo IP sorgente
    dst_ip = socket.inet_ntoa(unpacked[9])  # Indirizzo IP destinazione

    return src_ip, dst_ip

def start_sniffer():
    try:
        # Creazione del socket RAW (AF_PACKET intercetta tutti i pacchetti Ethernet)
        sniffer_socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0800))

        print("\nSniffer attivo su Linux! In attesa di pacchetti...\n")

        while True:
            raw_packet, _ = sniffer_socket.recvfrom(65565)  # Riceve pacchetti grezzi
            src_ip, dst_ip = parse_ip_header(raw_packet)  # Analizza il pacchetto

            print("=" * 60)
            print(f"**Mittente (IP Sorgente):** {src_ip}")
            print(f"**Destinatario (IP Destinazione):** {dst_ip}")
            print("=" * 60)

    except PermissionError:
        print("Errore di permessi! Avvia il programma con privilegi di root (sudo).")
    except KeyboardInterrupt:
        print("\nSniffer terminato.")

if __name__ == "__main__":
    start_sniffer()
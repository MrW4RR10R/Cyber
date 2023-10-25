import socket


def scan_ports(target, start_port, end_port):
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Imposta il timeout per la connessione

        try:
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is open")
            else:
                print(f"Port {port} is closed")
        except socket.error:
            print(f"Port {port} is closed")
        finally:
            sock.close()


if __name__ == '__main__':
    target = input("Inserisci l'indirizzo IP del dispositivo da scansionare: ")
    start_port = 1  # Porta iniziale
    end_port = 100  # Porta finale

    scan_ports(target, start_port, end_port)
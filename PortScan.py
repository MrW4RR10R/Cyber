from socket import *

tgtHost = input('Inserire indirizzo: \n')
tgtPort = int(input('inserire la porta fa controllare: \n'))


def ScanConnessione(tgtHost, tgtPort):
    try:
        socketconnessione= socket(AF_INET, SOCK_STREAM)
        socketconnessione.connect(tgtHost, tgtPort)
        print('[+]%d -> top aperta' % tgtPort)
        socketconnessione.close()
    except:
        print('[-]%d -> top chiusa' % tgtPort)

def ScanIndirizzo(tgtHost, tgtPort):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print('[-]Indirizzo inesistente %s' % tgtHost)
    try:
        tgtNome = gethostbyaddr(tgtIP)
        print('\n[+] Scan Indirizzo: %s' % tgtNome[0])
    except:
        print('\n[+] Scan Indirizzo: %s' % tgtIP)
        setdefaulttimeout(1)
        print('Scansione Porta: %d' % tgtPort)
        ScanConnessione(tgtHost, tgtPort)


if __name__ == '__main__':
    ScanIndirizzo(tgtHost, tgtPort)

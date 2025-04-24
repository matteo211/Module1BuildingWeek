import socket

# controlla se le porte inserite sono valide 
def port_valid(port):
    if not(0 < port <= 65535):
        return False

    return True

ip_target = input("inserisci ip target: ")

while True:
    try:
        low_port = int(input("inserisci porta di partenza: "))
        if not port_valid(low_port): # se l'input e' invalido ripeti il ciclo
            print("porta invalida, riprovare")
            continue

        high_port = int(input("inserisci porta finale:"))
        if not port_valid(high_port):
            print("porta invalida, riprovare")
            continue
        
        # se l'input e' valido l'esecuzione arriva qui e stoppa il ciclo
        break
    except ValueError:
        print("inserire solo numeri interi\n")

open_port_list = []

print("\nscannerizzando ", ip_target, " da porta ", low_port, " a porta ", high_port)

for port in range(low_port, high_port + 1):
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    status = sock.connect_ex((ip_target, port))

    if status == 0: 
        print(f"porta {port} = APERTA")
        open_port_list.append(port) 
    else: 
        print(f"porta {port} = CHIUSA")
    
    sock.close()

print("\nRIEPILOGO DELLE PORTE APERTE")
for port in open_port_list:
    print(port)
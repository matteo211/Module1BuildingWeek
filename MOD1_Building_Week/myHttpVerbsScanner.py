import socket

# target informations
ip_target = "192.168.20.10"
port_target = 80
path_target = "/phpMyAdmin/"  

# verbi http da testare
http_verbs = ["GET", "POST", "PUT", "DELETE", "OPTIONS", "HEAD", "TRACE", "CONNECT", "PATCH", "LINK", "UNLINK", "PROPFIND"]

print(f"Test dei verbi su http://{ip_target}{path_target}\n")

for verb in http_verbs:
    print(f"verbo: {verb}")

    # OPTIONS request
    """
    nel protocollo HTTP ogni riga deve finire con \r\n
    esempio di rischiesta ben formattata:

    OPTIONS /phpMyAdmin/ HTTP/1.1\r\n
    Host: 192.168.20.10\r\n
    Connection: close\r\n
    \r\n
    """
    request = f"{verb} {path_target} HTTP/1.1\r\nHost: {ip_target}\r\nConnection: close\r\n\r\n"
    
    # crea il socket e connetti al web server
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip_target, port_target))
    sock.send(request.encode())
 
    # uso 'b' per indicare che e' una stringa di dati da decodificare
    response = b""
    while True:
        data = sock.recv(1024)
        if not data:
            break
        response += data

    decoded_response = response.decode("utf-8")
    print(decoded_response.split("\r\n")[0])  # stampa solo la prima riga (status code)
    print()

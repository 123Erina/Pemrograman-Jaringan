import socket

# Konfigurasi server tujuan
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 12345

# Membuat socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Ketik 'exit' untuk keluar.\n")

while True:
    pesan = input("Kirim pesan ke server: ")
    if pesan.lower() == "exit":
        print("Keluar dari client.")
        break

    # Kirim pesan ke server
    client_socket.sendto(pesan.encode('utf-8'), (SERVER_HOST, SERVER_PORT))

    # Terima balasan dari server
    data, _ = client_socket.recvfrom(1024)
    print("Balasan server:", data.decode('utf-8'))

import socket
import datetime

# Konfigurasi server
HOST = "127.0.0.1"  # alamat lokal
PORT = 12345        # port bebas di atas 1024

# Membuat socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print(f"📡 Server UDP aktif di {HOST}:{PORT}")
print("Menunggu pesan dari client...\n")

# Loop agar server terus berjalan (tidak tutup koneksi)
while True:
    # Menerima data dari client
    data, addr = server_socket.recvfrom(1024)  # buffer 1024 byte
    message = data.decode('utf-8')
    waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Mencatat pesan ke file log
    with open("server_log.txt", "a") as log_file:
        log_file.write(f"[{waktu}] Dari {addr}: {message}\n")

    print(f"[{waktu}] Pesan dari {addr}: {message}")

    # Kirim balasan ke client
    balasan = f"Pesan diterima pada {waktu}"
    server_socket.sendto(balasan.encode('utf-8'), addr)

import socket
import struct
import time

def get_ntp_time(host="172.27.184.117"):
    # Menyiapkan paket NTP dengan versi 3
    msg = b'\x1b' + 47 * b'\0'
    TIME1970 = 2208988800  # Waktu NTP mulai dari tahun 1900, sementara Unix epoch dari tahun 1970

    try:
        print("Waktu mengirim ke server NTP (T1): ", time.time())
        # Membuat koneksi socket ke server NTP
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
            client.settimeout(5)
            client.sendto(msg, (host, 123))  # Kirim ke port NTP 123
            data, _ = client.recvfrom(1024)

        if data:
            # Memproses respons dari server NTP
            print("Waktu data sampai ke client (T4): ", time.time())
            unpacked_data = struct.unpack('!12I', data)
            ntp_time = unpacked_data[10] - TIME1970
            return time.ctime(ntp_time)
    except Exception as e:
        return f"Gagal mendapatkan waktu dari server NTP: {e}"

if __name__ == "__main__":
    print("Waktu dari NTP server:", get_ntp_time())
# Soal 5

import os
import csv
import json
import logging

# Logging setup (INFO untuk mulai/sukses, ERROR jika gagal)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    try:
        logging.info("Program mulai...")

        # Membuat folder data
        os.makedirs("data", exist_ok=True)  

        # Menulis file CSV data/presensi.csv (3 baris data)
        csv_path = "data/presensi.csv"
        with open(csv_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["nim", "nama", "hadir_uts"])
            writer.writerow(["230103256", "Ivan", 1])
            writer.writerow(["230103132", "Egie", 0])
            writer.writerow(["230103140", "Linlin", 1])
        logging.info("File CSV berhasil dibuat.")

        # Membaca kembali CSV, hitung total, hadir, dan persentase
        total = 0
        hadir = 0
        try:
            with open(csv_path, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    total += 1
                    if int(row["hadir_uts"]) == 1:
                        hadir += 1
        except Exception as e:
            logging.error(f"Gagal membaca CSV: {e}")
            return

        # Hitung persentase
        persentase = (hadir / total * 100) if total > 0 else 0

        # Simpan hasil ke JSON
        hasil = {
            "total_mahasiswa": total,
            "hadir": hadir,
            "persentase_hadir": persentase
        }

        json_path = "data/ringkasan.json"
        try:
            with open(json_path, mode="w", encoding="utf-8") as jf:
                json.dump(hasil, jf, indent=4)
        except Exception as e:
            logging.error(f"Gagal menyimpan JSON: {e}")
            return

        logging.info("Rekap berhasil disimpan ke data/ringkasan.json")
        logging.info("Program selesai dengan sukses ✅")

    except Exception as e:
        logging.error(f"Terjadi kesalahan umum: {e}")


if __name__ == "__main__":
    main()
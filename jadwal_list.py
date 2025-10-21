# Soal 4

def jadwal_hari(hari):
    """
* Menampilkan jadwal kuliah berdasarkan hari yang diminta.
* Pencarian dilakukan dengan mengecek satu per satu isi list dalam dictionary.
    """
    jadwal = {
        "Senin": ["Pengantar IoT", "Bahasa Inggris"],
        "Selasa": ["Pemrograman Python", "Teknik Digital"],
        "Rabu": ["Basis Data", "Jaringan Komputer"],
        "Kamis": ["Sistem Operasi", "Kewirausahaan"],
        "Jumat": ["Pengantar IoT"]
    }

    if hari in jadwal:
        print(f"Jadwal hari {hari}: {', '.join(jadwal[hari])}")
    else:
        print("Hari tidak ditemukan dalam jadwal.")
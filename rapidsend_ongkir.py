# Soal 3

def hitung_ongkir(berat_kg, kota, asuransi=False):
    """
    Menghitung ongkos kirim berdasarkan kota, berat (kg), dan opsi asuransi.
    Return : Ongkir
    """
    tarif_dasar = {
        "Jakarta": 15000,
        "Bandung": 12000,
        "Surabaya": 11000,
        "Yogyakarta": 10000,
        "Surakarta": 7000
    }

    if kota not in tarif_dasar:
        return "Kota tidak ditemukan."

    ongkir = tarif_dasar[kota] + 2000 * berat_kg

    if asuransi:
        ongkir += 3000

    return ongkir
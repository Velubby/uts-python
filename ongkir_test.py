from rapidsend_ongkir import hitung_ongkir


print(hitung_ongkir.__doc__)
# Test 1: tanpa asuransi
print(hitung_ongkir(3, "Jakarta"))  

# Test 2: dengan asuransi
print(hitung_ongkir(5, "Yogyakarta", True)) 

# Test 3: Kota tidak Valid
print(hitung_ongkir(2,"Solo", True))
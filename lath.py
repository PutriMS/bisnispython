print('     TIKET BUS      ')
print('-'*20)
print('Kode Kota :')
print('1. Prabumulih')
print('2. Muara Enim')
print('3. Lumbuklinggau')
kota = int(input('Pilihan Kota (1/2/3) \t: '))
print('Kode Kelas :')
print('1. Ekonomi')
print('2. Bisnis')
print('3. Eksekutif')
kelas = int(input('Pilihan kelas (1/2/3) \t: '))
jumlah = int(input('Masukkan banyak tiket \t: '))

if kota == 1 :
  if kelas == 1 :
    harga = 100000
  elif kelas == 2 :
    harga = 400000
  elif kelas == 3 :
    harga = 700000
elif kota == 2 :
  if kelas == 1 :
    harga = 200000
  elif kelas == 2 :
    harga = 500000
  elif kelas == 3 :
    harga = 800000
elif kota == 3 :
  if kelas == 1 :
    harga = 300000
  elif kelas == 2 :
    harga = 600000
  elif kelas == 3 :
    harga = 900000

if kota == 2 and kelas == 1 :
  diskon = input('Kode promo = ')
elif kota == 3 and kelas == 3 :
  diskon = input('Kode promo = ')
else :
  diskon = 0

print('-'*20)
print(f'Harga tiket \t: {harga}')
subtotal = int(harga * jumlah)
if diskon == 'igs' :
  discount = int(0.1 * subtotal)
else : 
  discount = 0
totalbayar = subtotal - discount
print(f'Subtotal \t: {subtotal}')
print(f'Discount \t: {discount}')
print(f'Total Bayar \t: {totalbayar}')
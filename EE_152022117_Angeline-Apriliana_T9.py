import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)
 
# Pertanyaan 1:

# Gunakan loop for dan fungsi lambda untuk menghitung gaji setiap karyawan setelah diberikan peningkatan sebesar 5% dari gaji saat ini.

peningkatan_lima_persen = lambda gaji: gaji + (gaji * 0.05) # Fungsi lambda untuk menghitung gaji setelah peningkatan 5%

for index, row in df.iterrows(): # Loop for untuk menerapkan fungsi lambda pada setiap nilai gaji dalam dataframe
    df.at[index, 'Gaji'] = peningkatan_lima_persen(row['Gaji'])

# Pertanyaan 2:

# Setelah perubahan dilakukan, tampilkan DataFrame yang sudah diperbarui dan berikan ringkasan perubahan yang telah terjadi.

# Menampilkan DataFrame yang sudah diperbarui
print("DataFrame setelah diperbarui:")
print(df)

# Ringkasan perubahan
print("\nRingkasan Perubahan:")
perubahan = pd.DataFrame(data)[['Gaji']].rename(columns={'Gaji': 'Gaji Awal'})
perubahan['Gaji Setelah Diperbarui'] = df['Gaji']
print(perubahan)
# Pertanyaan 3:

# Gunakan loop for lagi untuk mengevaluasi karyawan yang usianya di atas 30 tahun. 
# Jika usia karyawan di atas 30, berikan peningkatan tambahan sebesar 2% dari gaji saat ini menggunakan fungsi lambda.

# Fungsi lambda untuk menghitung peningkatan tambahan 2% jika usia di atas 30 tahun
peningkatan_dua_persen = lambda gaji, usia: gaji + (gaji * 0.02) if usia > 30 else gaji

# Gunakan loop for untuk menerapkan fungsi lambda pada setiap nilai gaji dalam dataframe
for index, row in df.iterrows():
    df.at[index, 'Gaji'] = peningkatan_dua_persen(row['Gaji'], row['Usia'])
print('')
# Pertanyaan 4:

# Tampilkan DataFrame yang sudah diperbarui setelah peningkatan gaji tambahan dan berikan ringkasan hasilnya.

# Menampilkan DataFrame yang sudah diperbarui setelah peningkatan tambahan
print("DataFrame setelah peningkatan tambahan:")
print(df)

print('')

# Ringkasan perubahan gaji sebelum dan sesudah peningkatan dua persen
perubahan = pd.DataFrame(data)[['Gaji']].rename(columns={'Gaji': 'Gaji Awal'})
perubahan['Gaji Setelah Peningkatan 5%'] = perubahan['Gaji Awal'] + (perubahan['Gaji Awal'] * 0.05)
perubahan['Gaji Setelah Peningkatan 2% (Umur >30)'] = df['Gaji']
print(perubahan)

# ---------------------------- #
# Buat Branch Baru pada repository github berikut dengan format KELAS_NRP_NAMA
# https://github.com/diashfirdaus-cyber/Pemdas_Itenas.git
# ---------------------------- #

# Catatan:

# Gunakan loop for dan fungsi lambda untuk mengimplementasikan operasi yang diminta.
# Pastikan untuk menyimpan hasil perubahan pada DataFrame.
# Tampilkan hasil dan ringkasan dengan jelas.
# Jangan lupa untuk menyesuaikan persentase peningkatan gaji sesuai dengan cerita.
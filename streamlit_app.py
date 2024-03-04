import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Menambahkan informasi tugas akhir
st.title('Tugas Akhir Belajar Analisis Data dengan Python')
st.write("Nama : Arya Pradipto")
st.write("Email : M006D4KY2375@bangkit.academy")

# Data untuk analisis permintaan musiman
data_musim = {
    'Musim': ['Spring', 'Summer', 'Fall', 'Winter'],
    'Jumlah_Sewa': [644.798906, 1256.619699, 1451.612859, 1151.317373]
}

# Membuat DataFrame untuk permintaan musiman
df_musim = pd.DataFrame(data_musim)
rata_rata_musim = df_musim['Jumlah_Sewa']

# Visualisasi permintaan musiman menggunakan matplotlib
st.write("\n\n\n\n\n")
st.write("Pertanyaan 1 = Bagiamana variasi permintaan sewa pada berbagai musim?")
plt.figure(figsize=(10, 6))
rata_rata_musim.plot(kind='bar', color='lightseagreen')
plt.title('Jumlah Sewa Sepeda per Musim')
plt.xlabel('Musim')
plt.ylabel('Jumlah Sewa Sepeda') 
plt.xticks(ticks=[0, 1, 2, 3], labels=['semi', 'panas', 'gugur', 'dingin'])
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot(plt)
st.write("Seperti yang bisa dilihat pada grafik nya, bahwa ternyata Musim yang paling banyak menyewa sepeda nya adalah pada musim gugur dengan angka rata-rata 1452. Diangka kedua adalah musim panas dengan rata-rata 1257. Selanjutnya pada bulan ketiga adalah musim dingin dengan angka rata-rata 1151, dan yang terakhir musim semi dengan angka rata-rata 645.")

# Data untuk analisis pengaruh kondisi cuaca terhadap sewa sepeda
data_cuaca = {
    'Kondisi_Cuaca': ['Clear', 'Mist', 'Light Snow', 'Heavy Rain'],
    'Rata_Rata_Jumlah_Sewa': [204.869272, 175.165493, 111.579281, 74.333333]
} 

# Membuat DataFrame untuk kondisi cuaca
df_cuaca = pd.DataFrame(data_cuaca)
demand_cuaca = df_cuaca['Rata_Rata_Jumlah_Sewa']

# Visualisasi pengaruh kondisi cuaca menggunakan matplotlib
st.write("\n" * 10)
st.write ("Pertanyaan 2 = Bagiamana faktor cuaca seperti suhu, kelembaban, dan kecepatan angin mempengatuhi penggunaan sepeda nya?")
plt.figure(figsize=(10, 6))
demand_cuaca.plot(kind='bar', color='thistle')
plt.title('Rata-Rata Jumlah Sewa Sepeda Berdasarkan Kondisi Cuaca')
plt.xlabel('Kondisi Cuaca')
plt.ylabel('Rata-Rata Jumlah Sewa Sepeda')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
notes = "1 = Clear, Few clouds, partly cloudy \n2 = Mist + Cloudy, Mist + Broken Clouds, Mist + Few clouds, Mist\n3 = Light snow, Light Rain + Thunderstorm + Scattered Clouds, Light Rain + Scattered clouds \n4 = Heavy rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog"
plt.text(0.1, -0.3, notes, fontsize=10, ha='left', va='bottom', transform=plt.gca().transAxes)
st.pyplot(plt)
st.write("**Conclution Pertanyaan 2** = Pada rata-rata jumlah sewa sepeda berdasarkan kondisi cuaca, cuaca yang paling banyak penyewa nya adalah cuaca **Clear, Few clouds, partly**. Lalu cuaca yang kedua adalah cuaca **Mist + Cloudy, Mist + Broken Clouds, Mist + Few clouds, Mist**. Cuaca ketiga yang paling banyak disewa adalah cuaca **Light snow, Light Rain + Thunderstorm + Scattered Clouds, Light Rain + Scattered clouds**. Dan yang terakhir adalah **Heavy rain + Ice Pallets + thunderstorm + Mist, Snow + Fog**.")

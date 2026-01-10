# 🧠 MindMetric Pro

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B)
![Machine Learning](https://img.shields.io/badge/Scikit--Learn-Model-orange)
![Status](https://img.shields.io/badge/Status-Active-success)

**Sistem Analisis & Deteksi Dini Kesehatan Mental Mahasiswa Berbasis Machine Learning.**

## 📋 Tentang Project
**MindMetric Pro** adalah aplikasi web interaktif yang dirancang untuk mendeteksi potensi risiko depresi pada mahasiswa. Aplikasi ini menganalisis pola kesehatan mental berdasarkan data demografis, akademik (IPK), dan riwayat gejala klinis.

Project ini dikembangkan sebagai tugas **Ujian Akhir Semester (UAS)** mata kuliah Machine Learning.

### ✨ Fitur Unggulan
1.  **⚙️ Dual-Engine AI:** Pengguna dapat memilih dan membandingkan dua algoritma prediksi:
    * 🌲 **Random Forest Classifier** (Akurasi Tinggi & Stabil)
    * 📈 **Logistic Regression** (Efisien & Probabilistik)
2.  **📊 Interactive Dashboard:** Dilengkapi grafik visual (*Pie Chart* & *Bar Chart*) untuk membandingkan posisi pengguna dengan statistik populasi kampus.
3.  **🧠 Smart Preprocessing:** Menggunakan teknik *binning* pada data IPK untuk hasil analisis yang lebih objektif.
4.  **⚡ Real-time Analysis:** Hasil prediksi risiko dan persentase probabilitas muncul seketika.

---

## 📸 Tampilan Aplikasi (Screenshots)

![Dashboard Preview](path/to/your/screenshot.png)

---

## 🛠️ Teknologi yang Digunakan
* **Bahasa Pemrograman:** Python
* **Web Framework:** Streamlit
* **Machine Learning:** Scikit-Learn
* **Data Processing:** Pandas, NumPy
* **Visualisasi Data:** Plotly Express

---

## 📂 Struktur Folder
```text
MindMetric-Pro/
├── aplikasi.py          # File utama (Frontend Streamlit)
├── model.py             # Script untuk melatih & menyimpan model AI
├── model_rf.pkl         # Otak AI (Random Forest)
├── model_lr.pkl         # Otak AI (Logistic Regression)
├── Student Mental health.csv  # Dataset
├── requirements.txt     # Daftar library yang dibutuhkan
└── README.md            # Dokumentasi ini

```

---

## 🚀 Cara Menjalankan (Installation)

Ikuti langkah-langkah ini untuk menjalankan aplikasi di komputer lokal Anda:

1. **Clone Repository ini:**
```
git clone [https://github.com/USERNAME_KAMU/MindMetric-UAS.git](https://github.com/USERNAME_KAMU/MindMetric-UAS.git)
cd MindMetric-UAS

```


2. **Install Library yang dibutuhkan:**
```
pip install -r requirements.txt

```


3. **Latih Model (Wajib dilakukan pertama kali):**
Jalankan script ini untuk menghasilkan file `.pkl`:
```
python model.py
```


*(Pastikan muncul pesan sukses bahwa model_rf.pkl dan model_lr.pkl berhasil dibuat)*
4. **Jalankan Aplikasi:**
```
python -m streamlit run aplikasi.py
```




---

## 📊 Tentang Dataset

Dataset yang digunakan berasal dari survei kesehatan mental mahasiswa (sumber: Kaggle).

* **Total Data:** 101 Mahasiswa (sebelum *preprocessing*)
* **Fitur Input:** Gender, Usia, Tahun Kuliah, Status Pernikahan, IPK (CGPA), Riwayat Kecemasan (Anxiety), Riwayat Panic Attack.
* **Target Output:** Depresi (Ya/Tidak).

---

## ⚠️ Disclaimer

Aplikasi ini merupakan simulasi Machine Learning untuk tujuan **Edukasi & Akademik**. Hasil prediksi hanyalah probabilitas statistik dan **TIDAK 100% AKURAT**. Aplikasi ini bukan pengganti diagnosa medis profesional. Jika Anda merasa membutuhkan bantuan, segera hubungi psikolog atau psikiater.

---

## 👨‍💻 Author

**Nabil Deja**

* Universitas Bina Insani
* Jurusan: Rekayasa Perangkat Lunak

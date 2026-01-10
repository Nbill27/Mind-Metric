import streamlit as st
import pickle
import pandas as pd
import plotly.express as px

# 1. Konfigurasi Halaman (Wide Layout)
st.set_page_config(
    page_title="MindMetric Pro",
    page_icon="🧠",
    layout="wide"
)

# 2. Load Model & Dataset
try:
    with open('model_rf.pkl', 'rb') as f:
        model_rf = pickle.load(f)
    with open('model_lr.pkl', 'rb') as f:
        model_lr = pickle.load(f)
    
    # Load data asli untuk grafik dashboard
    df_asli = pd.read_csv('Student Mental health.csv')
    df_asli.columns = ['Timestamp', 'Gender', 'Age', 'Course', 'Year', 'CGPA', 'Marital_Status', 'Depression', 'Anxiety', 'Panic_Attack', 'Treatment']
except FileNotFoundError:
    st.error("⚠️ File model/dataset tidak ditemukan. Jalankan 'bikin_model.py' dulu!")
    st.stop()

# 3. Sidebar (Kontrol Panel)
st.sidebar.title("⚙️ Panel Kontrol")
st.sidebar.write("Pilih Algoritma AI:")
pilihan_model = st.sidebar.selectbox("Model", ("Random Forest", "Logistic Regression"))

if pilihan_model == "Random Forest":
    model_aktif = model_rf
    st.sidebar.success(f"✅ Aktif: {pilihan_model}")
    st.sidebar.caption("Keunggulan: Akurasi tinggi & stabil (Ensemble).")
else:
    model_aktif = model_lr
    st.sidebar.info(f"✅ Aktif: {pilihan_model}")
    st.sidebar.caption("Keunggulan: Cepat & probabilistik.")

st.sidebar.markdown("---")
st.sidebar.write("© 2025 MindMetric Project")

# ==========================================
# BAGIAN ATAS: INTRO
# ==========================================
st.title("🧠 MindMetric Pro")
st.markdown("### Sistem Deteksi Dini Kesehatan Mental Mahasiswa")

with st.expander("ℹ️ Tentang Aplikasi Ini (Klik untuk baca)", expanded=True):
    st.write("""
    **Selamat datang!** 👋
    Aplikasi ini menggunakan **Machine Learning** untuk menganalisis risiko depresi pada mahasiswa berdasarkan pola akademik dan gejala klinis.
    
    **Fitur Utama:**
    * 🔍 **Dual-Engine:** Pilih antara Random Forest atau Logistic Regression.
    * 📊 **Data Insight:** Lihat statistik perbandingan dengan mahasiswa lain.
    * 🛡️ **Privasi:** Data yang diinput tidak disimpan permanen.
    """)

st.write("---")

# ==========================================
# LAYOUT UTAMA (KIRI: INPUT, KANAN: HASIL)
# ==========================================
col_kiri, col_kanan = st.columns([1, 1.5])

# --- INPUT USER ---
with col_kiri:
    st.header("📝 1. Isi Data Diri")
    
    gender = st.selectbox("Jenis Kelamin", ("Laki-laki", "Perempuan"))
    gender_val = 1 if gender == "Laki-laki" else 0
    
    age = st.number_input("Usia (Tahun)", 17, 30, 20)
    
    year = st.selectbox("Tahun Kuliah", ("Tahun 1", "Tahun 2", "Tahun 3", "Tahun 4", "Akhir"))
    year_val = int(year.split()[1]) if "Tahun" in year else 5
    
    marital = st.selectbox("Status Pernikahan", ("Belum", "Sudah"))
    marital_val = 1 if marital == "Sudah" else 0
    
    # Input IPK (Sesuai Logic Binning)
    cgpa = st.selectbox("IPK Terakhir", 
        ("IPK Tinggi (> 3.00)", "IPK Menengah (2.50 - 2.99)", "IPK Rendah (< 2.50)"))
    
    # Mapping Nilai ke Angka
    if "Tinggi" in cgpa: cgpa_val = 3.50
    elif "Menengah" in cgpa: cgpa_val = 2.75
    else: cgpa_val = 2.00
    
    st.markdown("---")
    st.subheader("Gejala Klinis")
    anxiety = st.radio("Sering merasa cemas/gelisah?", ("Tidak", "Ya"), horizontal=True)
    panic = st.radio("Pernah serangan panik?", ("Tidak", "Ya"), horizontal=True)
    
    anxiety_val = 1 if anxiety == "Ya" else 0
    panic_val = 1 if panic == "Ya" else 0
    
    st.write("")
    tombol = st.button("🚀 Analisa Sekarang", use_container_width=True)

# --- HASIL & DASHBOARD ---
with col_kanan:
    if tombol:
        # A. PREDIKSI
        st.header("📊 2. Hasil Analisa")
        
        input_data = [[age, gender_val, cgpa_val, year_val, marital_val, anxiety_val, panic_val]]
        hasil = model_aktif.predict(input_data)[0]
        prob = model_aktif.predict_proba(input_data)[0][1] * 100
        
        if hasil == 1:
            st.error(f"⚠️ **TERDETEKSI RISIKO TINGGI ({prob:.1f}%)**")
            st.write(f"Model **{pilihan_model}** mendeteksi pola yang mengarah pada kondisi depresi. Disarankan konsultasi.")
        else:
            st.success(f"✅ **KONDISI STABIL ({prob:.1f}%)**")
            st.write(f"Model **{pilihan_model}** menilai kesehatan mental Anda terjaga dengan baik.")
        
        st.caption("⚠️ *Angka ini adalah probabilitas statistik AI, bukan diagnosa medis mutlak.*")
        st.write("---")
        
        # B. DASHBOARD GRAFIK
        st.subheader("📈 Data Insight Kampus")
        
        tab1, tab2 = st.tabs(["Distribusi Depresi", "Analisa IPK"])
        
        with tab1:
            st.caption("Proporsi Mahasiswa Depresi vs Sehat di Dataset")
            pie_data = df_asli['Depression'].value_counts()
            fig1 = px.pie(values=pie_data.values, names=pie_data.index, 
                          color_discrete_sequence=['#636EFA', '#EF553B'], hole=0.4)
            st.plotly_chart(fig1, use_container_width=True)
            
        with tab2:
            st.caption("Hubungan Kelompok IPK dengan Tingkat Depresi")
            # Logic Binning untuk Grafik (Biar sama dengan input)
            def kelompokkan_ipk(x):
                x = str(x).strip()
                if x == '3.50 - 4.00' or x == '3.00 - 3.49': return 'IPK Tinggi (> 3.00)'
                elif x == '2.50 - 2.99': return 'IPK Menengah (2.50 - 2.99)'
                else: return 'IPK Rendah (< 2.50)'
            
            df_asli['Kelompok_IPK'] = df_asli['CGPA'].apply(kelompokkan_ipk)
            
            # Plot Bar Chart
            fig2 = px.histogram(df_asli, x="Kelompok_IPK", color="Depression", 
                                barmode="group",
                                color_discrete_map={"Yes": "#EF553B", "No": "#00CC96"},
                                category_orders={"Kelompok_IPK": ["IPK Rendah (< 2.50)", "IPK Menengah (2.50 - 2.99)", "IPK Tinggi (> 3.00)"]})
            st.plotly_chart(fig2, use_container_width=True)

    else:
        st.info("👈 Silakan lengkapi data di samping untuk melihat hasil prediksi & grafik statistik.")

# ==========================================
# DISCLAIMER FOOTER
# ==========================================
st.write("")
st.markdown("---")
st.warning("""
**⚠️ DISCLAIMER PENTING:** Aplikasi ini adalah simulasi Machine Learning untuk tujuan akademik. 
Hasil prediksi **TIDAK 100% AKURAT**. Jika Anda merasa butuh bantuan, segera hubungi profesional.
""")
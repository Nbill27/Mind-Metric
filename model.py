import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# ==========================================
# 1. LOAD DATASET
# ==========================================
filename = 'Student Mental health.csv'
try:
    df = pd.read_csv(filename)
    print("✅ Data berhasil dibaca!")
except FileNotFoundError:
    print(f"❌ Error: File '{filename}' tidak ditemukan. Pastikan file ada di folder ini.")
    exit()

# Ganti nama kolom biar enak
df.columns = ['Timestamp', 'Gender', 'Age', 'Course', 'Year', 'CGPA', 'Marital_Status', 
              'Depression', 'Anxiety', 'Panic_Attack', 'Treatment']

df = df.dropna()

# ==========================================
# 2. DATA CLEANING & BINNING (LOGIKA BARU)
# ==========================================

# Bersihkan Tahun
def clean_year(x):
    if isinstance(x, str):
        x = x.lower().replace('year', '').strip()
        try: return int(x)
        except: return 1
    return x

# Bersihkan IPK (Teknik Grouping/Binning)
# Kita gabung kategori biar data lebih valid dan grafik tidak merah semua
def clean_cgpa(x):
    if isinstance(x, str):
        x = x.strip()
        # Gabung 3.00 ke atas jadi satu kelompok "Tinggi" (Skor 3.50)
        if x == '3.50 - 4.00' or x == '3.00 - 3.49': 
            return 3.50 
        # Kelompok Menengah (Skor 2.75)
        elif x == '2.50 - 2.99': 
            return 2.75
        # Kelompok Bawah (Skor 2.00)
        else: 
            return 2.00
    return 3.50 # Default

df['Year'] = df['Year'].apply(clean_year)
df['CGPA'] = df['CGPA'].apply(clean_cgpa)
df['Gender'] = df['Gender'].map({'Female': 0, 'Male': 1})

# Ubah Yes/No jadi 1/0
for col in ['Marital_Status', 'Depression', 'Anxiety', 'Panic_Attack', 'Treatment']:
    df[col] = df[col].map({'Yes': 1, 'No': 0})

df = df.dropna()

# ==========================================
# 3. LATIH DUA MODEL SEKALIGUS
# ==========================================
X = df[['Age', 'Gender', 'CGPA', 'Year', 'Marital_Status', 'Anxiety', 'Panic_Attack']]
y = df['Depression']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model 1: Random Forest
print("Melatih Random Forest...")
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_acc = accuracy_score(y_test, rf_model.predict(X_test)) * 100

# Model 2: Logistic Regression
print("Melatih Logistic Regression...")
lr_model = LogisticRegression(random_state=42)
lr_model.fit(X_train, y_train)
lr_acc = accuracy_score(y_test, lr_model.predict(X_test)) * 100

print(f"\n=== HASIL AKURASI ===\nRF: {rf_acc:.2f}%\nLR: {lr_acc:.2f}%")

# ==========================================
# 4. SIMPAN MODEL
# ==========================================
with open('model_rf.pkl', 'wb') as f: pickle.dump(rf_model, f)
with open('model_lr.pkl', 'wb') as f: pickle.dump(lr_model, f)

print(" Sukses! File 'model_rf.pkl' dan 'model_lr.pkl' berhasil dibuat.")
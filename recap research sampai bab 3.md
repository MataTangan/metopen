# Ringkasan Diskusi dan Kerangka Penelitian Skripsi: Analisis Pola Anomali dan Settlement QRIS

Dokumen ini berisi rangkuman komprehensif dari seluruh diskusi konsultasi mengenai rancangan judul skripsi Sistem Informasi: **"Analisis Pola Anomali Transaksi dan Keterlambatan Settlement QRIS Menggunakan Exploratory Data Analysis (EDA) Terintegrasi Dashboard Business Intelligence pada UMKM"**.

---

## 1. Konsep Utama Penelitian

*   **Exploratory Data Analysis (EDA):** Pendekatan investigasi data tanpa asumsi awal kaku, membiarkan data mentah "berbicara" melalui visualisasi statistik guna menemukan tren tersembunyi, anomali, atau pola kegagalan sistem.
*   **Business Intelligence Dashboard (DBI):** Antarmuka visual interaktif (menggunakan Looker Studio, Tableau, atau Power BI) yang menerjemahkan ribuan baris log transaksi menjadi indikator peringatan dini (*alerts*) bagi pemilik UMKM.

---

## 2. Tujuan Penelitian

1.  **Menemukan Pola Anomali:** Mengidentifikasi anomali transaksi QRIS (seperti uji coba nominal kecil/Rp1 sebelum indikasi *fraud*, atau lonjakan status *pending* pada jam-jam tertentu).
2.  **Menganalisis Kinerja Settlement:** Mengukur rata-rata waktu keterlambatan pencairan dana dari penyedia layanan ke rekening merchant berdasarkan hari, jam, atau *issuer*.
3.  **Membangun Solusi Visual:** Merancang Dashboard BI sebagai instrumen pendukung keputusan manajerial bagi UMKM tanpa memerlukan rekapitulasi manual di Excel.

---

## 3. Jenis dan Sumber Data

Penelitian ini menggunakan pendekatan **Metode Campuran (Mixed Methods)** dengan porsi utama Kuantitatif Eksploratif:
*   **Data Kuantitatif Sekunder (80%):** Log file transaksional dalam format CSV/Excel yang diekstrak dari dasbor *merchant* QRIS selama 3–6 bulan.
*   **Data Kualitatif Primer (20%):** Wawancara kontekstual dengan pemilik usaha/kasir di awal untuk menangkap *pain points* dan di akhir untuk validasi pengguna (*User Acceptance*).

---

## 4. Variabel Penelitian (Fitur Data)

Dalam EDA, variabel dikelompokkan menjadi atribut data dan metrik alih-alih variabel bebas ($X$) dan terikat ($Y$):

### A. Raw Variables (Fitur Mentah)
*   `idt1`: *Transaction_ID* (ID unik transaksi).
*   `wkt1`: *Transaction_Timestamp* (Waktu transaksi).
*   `fin1`: *Transaction_Amount* (Nominal transaksi).
*   `sts1`: *Transaction_Status* (*Success*, *Failed*, *Pending*).
*   `prv2`: *Issuer* (Aplikasi pembayaran pembeli seperti DANA, BCA, OVO).
*   `wkt4`: *Settlement_Timestamp* (Waktu dana masuk ke rekening bank UMKM).

### B. Derived Variables (Fitur Turunan / Feature Engineering)
*   `ddur2`: *Settlement_Duration* (Selisih waktu antara *Settlement_Timestamp* dan *Transaction_Timestamp*).
*   `dwkt6`: *Business_Hour_Flag* (Penanda transaksi pada jam operasional).
*   `dnom7`: *Low_Value_Repetitive_Flag* (Penanda transaksi mikro berulang untuk deteksi anomali/fraud).

---

## 5. Hipotesis Eksploratif (Analytical Assumptions)

*   **Hipotesis Waktu Rawan:** Diduga terdapat lonjakan status transaksi *pending* atau gagal yang signifikan pada jam sibuk operasional (pukul 11.00–13.00).
*   **Hipotesis Kinerja Provider:** Diduga terdapat variasi signifikan pada rata-rata durasi *settlement* di antara berbagai *payment gateway* atau *issuer*.
*   **Hipotesis Anomali Nominal:** Diduga terdapat pola transaksi mikro berulang (misal: Rp1–Rp100) sebelum terjadinya anomali operasional atau indikasi rekayasa sosial.

---

## 6. Strategi Argumen di Hadapan Dosen Penguji

*   **Pertanyaan:** *"Mana Variabel X dan Y di skripsi kamu?"*
    *   **Jawaban:** *"Penelitian ini menggunakan Exploratory Data Analysis dan Data Mining, sehingga tidak mencari hubungan sebab-akibat antar variabel $X$ dan $Y$. Penelitian ini bersifat eksploratif untuk menemukan pola tersembunyi menggunakan Fitur Data (Data Features) dari log transaksi."*
*   **Pertanyaan:** *"Kenapa bukan skripsi ekonomi atau manajemen bisnis?"*
    *   **Jawaban:** *"Objek material penelitian ini bukan omzet atau rasio keuangan, melainkan integritas data, kegagalan sistem, dan manajemen risiko tata kelola TI (IT Governance) pada infrastruktur pembayaran digital."*
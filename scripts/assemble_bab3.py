from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent.parent
MAIN = ROOT / "Draft Proposal Skripsi Afza Muhammad 2404140047.md"
BAB3 = ROOT / "BAB III - Metode Penelitian.md"

main = MAIN.read_text(encoding="utf-8")
bab3 = BAB3.read_text(encoding="utf-8").strip() + "\n"

# --- 1. Replace Chapter III TOC block ---
toc_start = main.index("[BAB 3 METODE PENELITIAN")
toc_end = main.index("[DAFTAR PUSTAKA")
toc_new = """[BAB 3 METODE PENELITIAN](#metode-penelitian)

[3.1 Pendekatan, Jenis, dan Prosedur Penelitian](#31-pendekatan-jenis-dan-prosedur-penelitian)

[3.2 Lokasi Penelitian](#32-lokasi-penelitian)

[3.3 Populasi dan Sampel](#33-populasi-dan-sampel)

[3.4 Variabel Penelitian dan Definisi Operasional](#34-variabel-penelitian-dan-definisi-operasional)

[3.5 Hipotesis Statistik](#35-hipotesis-statistik)

[3.6 Data dan Sumber Data](#36-data-dan-sumber-data)

[3.7 Teknik Pengumpulan Data](#37-teknik-pengumpulan-data)

[3.8 Teknik Keabsahan Data](#38-teknik-keabsahan-data)

[3.9 Teknik Analisis Data](#39-teknik-analisis-data)

[3.10 Etika Penelitian](#310-etika-penelitian)

"""
main = main[:toc_start] + toc_new + main[toc_end:]

# --- 2. Replace Daftar Pustaka TOC block (remove template examples) ---
dp_start = main.index("[DAFTAR PUSTAKA")
lamp_start = main.index("[**Lampiran 1")
main = main[:dp_start] + "[DAFTAR PUSTAKA](#daftar-pustaka)\n\n" + main[lamp_start:]

# --- 3. Rebuild Daftar Tabel Chapter III entries ---
dt_start = main.index("# **DAFTAR TABEL**")
dg_start = main.index("# **DAFTAR GAMBAR**")
tables_new = """# **DAFTAR TABEL**

[Tabel 1.1 Penelitian Terdahulu yang Mendasari](#tabel-11-penelitian-terdahulu-yang-mendasari)  
[Tabel 3.1 Timeline Rencana Penelitian](#tabel-31-timeline-rencana-penelitian)  
[Tabel 3.2 Definisi Operasional Variabel](#tabel-32-definisi-operasional-variabel)  
[Tabel 3.3 Indikator, Instrumen, Skala, dan Sumber Data](#tabel-33-indikator-instrumen-skala-dan-sumber-data)  
[Tabel 3.4 Jenis dan Sumber Data](#tabel-34-jenis-dan-sumber-data)  
[Tabel 3.5 Matriks Keselarasan Rumusan Masalah, Data, dan Analisis](#tabel-35-matriks-keselarasan-rumusan-masalah-data-dan-analisis)  
[Tabel 3.6 Kisi-kisi Instrumen System Usability Scale](#tabel-36-kisi-kisi-instrumen-system-usability-scale)  
[Tabel 3.7 Klasifikasi Hambatan Pembayaran QRIS](#tabel-37-klasifikasi-hambatan-pembayaran-qris)  
[Tabel 3.8 Pedoman Interpretasi Skor SUS](#tabel-38-pedoman-interpretasi-skor-sus)  
[Tabel 3.9 Rencana Analisis Data](#tabel-39-rencana-analisis-data)  

"""
main = main[:dt_start] + tables_new + main[dg_start:]

# --- 4. Rebuild Daftar Gambar Chapter III entries ---
dg_start = main.index("# **DAFTAR GAMBAR**")
pend_start = main.index("1. #     **PENDAHULUAN**")
figs_new = """# **DAFTAR GAMBAR**

[Gambar 3.1 Prosedur Penelitian](#gambar-31-prosedur-penelitian)  
[Gambar 3.2 Alur Pengukuran Durasi dan Jumlah Langkah Transaksi](#gambar-32-alur-pengukuran-durasi-dan-jumlah-langkah-transaksi)  

"""
main = main[:dg_start] + figs_new + main[pend_start:]

# --- 5. Insert Chapter III after its heading ---
heading = "3. #     **METODE PENELITIAN** {#metode-penelitian}"
idx = main.index(heading) + len(heading)
main = main[:idx] + "\n\n" + bab3 + main[idx:]

# --- 6. Backup + write ---
backup = MAIN.with_suffix(".md.bak")
if not backup.exists():
    shutil.copy2(MAIN, backup)
MAIN.write_text(main, encoding="utf-8")
print("Wrote", MAIN)
print("Backup", backup)
print("Chapter III characters:", len(bab3))

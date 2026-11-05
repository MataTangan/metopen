from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT = Path(__file__).resolve().parent.parent / "figures"
OUT.mkdir(exist_ok=True)

NAVY = "#1f3b57"
BLUE = "#2e6f9e"
LIGHT = "#eaf2f8"
GRAY = "#5b6770"
GOLD = "#b8860b"


def box(ax, x, y, w, h, text, fc=LIGHT, ec=BLUE, fs=10, bold=False):
    p = FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                       boxstyle="round,pad=0.012,rounding_size=0.02",
                       linewidth=1.4, edgecolor=ec, facecolor=fc)
    ax.add_patch(p)
    ax.text(x, y, text, ha="center", va="center", fontsize=fs,
            color=NAVY, wrap=True, fontweight="bold" if bold else "normal")


def arrow(ax, x1, y1, x2, y2, color=GRAY):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2),
                                 arrowstyle="-|>", mutation_scale=14,
                                 linewidth=1.3, color=color,
                                 shrinkA=2, shrinkB=2))


# ---------------- Figure 3.1 ----------------
fig, ax = plt.subplots(figsize=(8.2, 12.4))
ax.set_xlim(0, 10)
ax.set_ylim(0, 20)
ax.axis("off")

stages = [
    ("1. Studi Pendahuluan dan Kajian Literatur\n(kerangka konseptual, definisi operasional, indikator)", 18.4),
    ("2. Penyusunan Instrumen\n(protokol observasi, lembar langkah/hambatan, kuesioner SUS, pedoman wawancara)", 16.3),
    ("3. Uji Coba Instrumen dan Perbaikan\n(kejelasan instruksi, konsistensi kategori, keterbacaan SUS)", 14.1),
    ("4. Penentuan UMKM dan Partisipan\n(purposif: QRIS statis dan dinamis, pelanggan dan kasir)", 11.9),
    ("5. Pengumpulan Data Kuantitatif\n(observasi transaksi, pencatatan durasi/langkah/keberhasilan/hambatan, kuesioner SUS)", 9.5),
    ("6. Analisis Awal Kuantitatif\n(deskriptif, skor SUS, identifikasi kasus ekstrem)", 7.3),
    ("7. Pengumpulan Data Kualitatif\n(wawancara semi-terstruktur, catatan lapangan, dokumentasi)", 5.3),
    ("8. Analisis Kualitatif dan Integrasi\n(analisis tematik, joint display, penjelasan pola kuantitatif)", 3.2),
    ("9. Perumusan Rekomendasi dan Pelaporan\n(matriks dampak–upaya, draf laporan)", 1.2),
]

# color bands: preparation, data collection, analysis
for i, (text, y) in enumerate(stages):
    if i <= 3:
        fc = "#eef5ee"
        ec = "#4a7c59"
    elif i <= 6:
        fc = LIGHT
        ec = BLUE
    else:
        fc = "#fdf3e3"
        ec = GOLD
    box(ax, 5, y, 8.8, 1.55, text, fc=fc, ec=ec, fs=9.3)

for i in range(len(stages) - 1):
    arrow(ax, 5, stages[i][1] - 0.80, 5, stages[i + 1][1] + 0.80)

# side labels
ax.text(0.38, 19.4, "PERSIAPAN", rotation=90, va="top", ha="center",
        fontsize=8.5, color="#4a7c59", fontweight="bold")
ax.text(0.38, 10.2, "PELAKSANAAN", rotation=90, va="center", ha="center",
        fontsize=8.5, color=BLUE, fontweight="bold")
ax.text(0.38, 2.4, "ANALISIS", rotation=90, va="center", ha="center",
        fontsize=8.5, color=GOLD, fontweight="bold")

ax.text(5, 0.15, "Gambar 3.1 Prosedur Penelitian", ha="center", va="bottom",
        fontsize=11, fontweight="bold", color=NAVY)

fig.tight_layout()
fig.savefig(OUT / "gambar-3.1-prosedur-penelitian.png", dpi=220,
            bbox_inches="tight", facecolor="white")
plt.close(fig)


# ---------------- Figure 3.2 ----------------
fig, ax = plt.subplots(figsize=(13.2, 5.6))
ax.set_xlim(0, 13.6)
ax.set_ylim(0, 6)
ax.axis("off")

ax.text(6.5, 5.55, "Alur Pengukuran Durasi dan Jumlah Langkah Transaksi",
        ha="center", va="center", fontsize=12.5, fontweight="bold", color=NAVY)
ax.text(6.5, 5.15, "Titik awal dan titik akhir yang sama digunakan untuk QRIS statis dan dinamis",
        ha="center", va="center", fontsize=9, color=GRAY, style="italic")

steps_static = [
    "Titik awal:\nkasir menyebut\ntotal",
    "Buka aplikasi\npembayaran",
    "Pindai\nkode QR",
    "Masukkan\nnominal",
    "Periksa nominal\ndan merchant",
    "Pilih metode &\nkonfirmasi",
    "Otorisasi\n(PIN/biometrik)",
    "Konfirmasi\nberhasil",
    "Titik akhir:\nkasir verifikasi",
]
steps_dynamic = [
    "Titik awal:\nkasir menyebut\ntotal",
    "Buka aplikasi\npembayaran",
    "Pindai\nkode QR",
    "Periksa nominal\ntetap dari merchant",
    "Pilih metode &\nkonfirmasi",
    "Otorisasi\n(PIN/biometrik)",
    "Konfirmasi\nberhasil",
    "Titik akhir:\nkasir verifikasi",
]

# static row
y_s = 3.45
x0, dx, w, h = 1.35, 1.33, 1.12, 1.05
for i, s in enumerate(steps_static):
    fc = "#eaf2f8" if i not in (0, len(steps_static) - 1) else "#dce9f2"
    ec = BLUE
    if i == 3:
        fc, ec = "#fdf3e3", GOLD
    box(ax, x0 + i * dx, y_s, w, h, s, fc=fc, ec=ec, fs=7.3)
    if i < len(steps_static) - 1:
        arrow(ax, x0 + i * dx + w / 2 + 0.01, y_s,
              x0 + (i + 1) * dx - w / 2 - 0.01, y_s)

# dynamic row: column 3 deliberately left empty (no nominal input)
y_d = 1.55
dynamic_cols = [0, 1, 2, 4, 5, 6, 7, 8]
for s, col in zip(steps_dynamic, dynamic_cols):
    fc = "#eaf2f8" if col not in (0, 8) else "#dce9f2"
    box(ax, x0 + col * dx, y_d, w, h, s, fc=fc, ec=BLUE, fs=7.3)
for a, b in zip(dynamic_cols[:-1], dynamic_cols[1:]):
    arrow(ax, x0 + a * dx + w / 2 + 0.01, y_d,
          x0 + b * dx - w / 2 - 0.01, y_d)

# dashed placeholder for skipped column
p = FancyBboxPatch((x0 + 3 * dx - w / 2, y_d - h / 2), w, h,
                   boxstyle="round,pad=0.012,rounding_size=0.02",
                   linewidth=1.0, edgecolor=GRAY, facecolor="white",
                   linestyle=(0, (4, 3)))
ax.add_patch(p)
ax.text(x0 + 3 * dx, y_d, "tidak perlu\ninput nominal", ha="center",
        va="center", fontsize=7.3, color=GRAY, style="italic")

ax.text(0.40, y_s, "QRIS\nSTATIS", ha="center", va="center", fontsize=9.2,
        fontweight="bold", color=GOLD)
ax.text(0.40, y_d, "QRIS\nDINAMIS", ha="center", va="center", fontsize=9.2,
        fontweight="bold", color=BLUE)

# highlight skipped step
ax.annotate("Langkah tambahan\npada QRIS statis",
            xy=(x0 + 3 * dx, y_s - h / 2 - 0.03), xytext=(x0 + 3 * dx, 4.72),
            ha="center", fontsize=8, color=GOLD,
            arrowprops=dict(arrowstyle="-|>", color=GOLD, lw=1.1))

ax.text(6.5, 0.35, "Gambar 3.2 Alur Pengukuran Durasi dan Jumlah Langkah Transaksi",
        ha="center", va="center", fontsize=10.5, fontweight="bold", color=NAVY)

fig.tight_layout()
fig.savefig(OUT / "gambar-3.2-alur-pengukuran.png", dpi=220,
            bbox_inches="tight", facecolor="white")
plt.close(fig)

print("Figures written to", OUT)

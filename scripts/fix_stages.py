from pathlib import Path

old1 = (
    "Prosedur penelitian disusun dalam tujuh tahap yang saling terkait. Tahap pertama adalah studi "
    "pendahuluan dan kajian literatur untuk memantapkan kerangka konseptual, definisi operasional, dan "
    "indikator pengukuran. Tahap kedua adalah penyusunan instrumen, yang meliputi protokol observasi "
    "transaksi, lembar pencatatan langkah dan hambatan, kuesioner SUS berbahasa Indonesia, pedoman "
    "wawancara semi-terstruktur, serta formulir persetujuan partisipan. Tahap ketiga adalah uji coba "
    "instrumen pada sejumlah kecil transaksi dan partisipan untuk memeriksa kejelasan instruksi, "
    "kelayakan waktu pengamatan, dan konsistensi kategori pengamatan."
)
new1 = (
    "Prosedur penelitian disusun dalam sembilan tahap yang saling terkait. Tahap pertama adalah studi "
    "pendahuluan dan kajian literatur untuk memantapkan kerangka konseptual, definisi operasional, dan "
    "indikator pengukuran. Tahap kedua adalah penyusunan instrumen, yang meliputi protokol observasi "
    "transaksi, lembar pencatatan langkah dan hambatan, kuesioner SUS berbahasa Indonesia, pedoman "
    "wawancara semi-terstruktur, serta formulir persetujuan partisipan. Tahap ketiga adalah uji coba "
    "instrumen pada sejumlah kecil transaksi dan partisipan untuk memeriksa kejelasan instruksi, "
    "kelayakan waktu pengamatan, dan konsistensi kategori pengamatan. Tahap keempat adalah penentuan "
    "UMKM dan partisipan berdasarkan kriteria purposif yang telah ditetapkan."
)
old2 = (
    "Tahap keempat adalah pengumpulan data kuantitatif melalui observasi transaksi QRIS statis dan "
    "dinamis serta pemberian kuesioner SUS kepada pelanggan dan kasir setelah transaksi selesai. Tahap "
    "kelima adalah analisis awal data kuantitatif untuk memperoleh gambaran deskriptif dan "
    "mengidentifikasi kasus ekstrem atau pola yang memerlukan penjelasan. Tahap keenam adalah "
    "pengumpulan data kualitatif melalui wawancara semi-terstruktur dengan informan yang dipilih secara "
    "purposif, dengan fokus pada pengalaman, hambatan, dan saran perbaikan. Tahap ketujuh adalah "
    "analisis kualitatif, integrasi temuan kuantitatif dan kualitatif, serta perumusan rekomendasi. Alur "
    "prosedur penelitian disajikan pada Gambar 3.1."
)
new2 = (
    "Tahap kelima adalah pengumpulan data kuantitatif melalui observasi transaksi QRIS statis dan "
    "dinamis serta pemberian kuesioner SUS kepada pelanggan dan kasir setelah transaksi selesai. Tahap "
    "keenam adalah analisis awal data kuantitatif untuk memperoleh gambaran deskriptif dan "
    "mengidentifikasi kasus ekstrem atau pola yang memerlukan penjelasan. Tahap ketujuh adalah "
    "pengumpulan data kualitatif melalui wawancara semi-terstruktur dengan informan yang dipilih secara "
    "purposif, dengan fokus pada pengalaman, hambatan, dan saran perbaikan. Tahap kedelapan adalah "
    "analisis kualitatif dan integrasi temuan kuantitatif dan kualitatif. Tahap kesembilan adalah "
    "perumusan rekomendasi dan penyusunan laporan. Alur prosedur penelitian disajikan pada Gambar 3.1."
)
old3 = """| 4 | Pengumpulan data kuantitatif | Data durasi, langkah, keberhasilan, hambatan, dan skor SUS | Minggu 4–6 |
| 5 | Analisis awal data kuantitatif | Statistik deskriptif dan daftar kasus yang perlu dijelaskan | Minggu 6–7 |
| 6 | Pengumpulan data kualitatif | Transkrip wawancara dan catatan lapangan | Minggu 7–8 |
| 7 | Analisis kualitatif, integrasi, dan pelaporan | Tema, *joint display*, rekomendasi, dan draf laporan | Minggu 8–10 |"""
new3 = """| 4 | Penentuan UMKM dan partisipan | Daftar UMKM dan partisipan yang memenuhi kriteria | Minggu 4 |
| 5 | Pengumpulan data kuantitatif | Data durasi, langkah, keberhasilan, hambatan, dan skor SUS | Minggu 4–6 |
| 6 | Analisis awal data kuantitatif | Statistik deskriptif dan daftar kasus yang perlu dijelaskan | Minggu 6–7 |
| 7 | Pengumpulan data kualitatif | Transkrip wawancara dan catatan lapangan | Minggu 7–8 |
| 8 | Analisis kualitatif dan integrasi | Tema, *joint display*, dan interpretasi | Minggu 8–9 |
| 9 | Perumusan rekomendasi dan pelaporan | Rekomendasi dan draf laporan | Minggu 9–10 |"""

for name in ["BAB III - Metode Penelitian.md", "Draft Proposal Skripsi Afza Muhammad 2404140047.md"]:
    p = Path(name)
    s = p.read_text(encoding="utf-8")
    assert old1 in s, name + " old1"
    assert old2 in s, name + " old2"
    assert old3 in s, name + " old3"
    s = s.replace(old1, new1).replace(old2, new2).replace(old3, new3)
    p.write_text(s, encoding="utf-8")
    print("updated", name)

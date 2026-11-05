import re
from pathlib import Path

s = Path("Draft Proposal Skripsi Afza Muhammad 2404140047.md").read_text(encoding="utf-8")
ch = s[s.index("3. #     **METODE PENELITIAN**"):]

print("=== CITATION GROUPS (parenthetical) ===")
for c in sorted(set(re.findall(r"\(([^()]*?\b(?:19|20)\d{2}[a-z]?)\)", ch))):
    print(" -", c)

print("\n=== NARRATIVE CITATIONS ===")
for m in re.finditer(
    r"([A-Z][A-Za-zÀ-ÿ’'\-]+(?: et al\.| & [A-Z][A-Za-zÀ-ÿ’'\-]+| dan [A-Z][A-Za-zÀ-ÿ’'\-]+)?)\s*\((?:19|20)\d{2}\)",
    ch,
):
    print(" -", m.group(0))

print("\n=== TABLES ===")
for m in re.finditer(r"\*\*Tabel (3\.\d+)[^\n]*", ch):
    print(" -", m.group(0))

print("\n=== FIGURES ===")
for m in re.finditer(r"\*\*Gambar (3\.\d+)[^\n]*", ch):
    print(" -", m.group(0))

print("\n=== BIBLIOGRAPHY ENTRIES ===")
bib = ch[ch.index("## **DAFTAR PUSTAKA**"):]
for line in bib.splitlines():
    if re.match(r"^[A-ZÀ-Ý][^.]", line) and "(19" in line or "(20" in line:
        print(" -", line[:110])

print("\n=== HEADINGS ===")
for line in ch.splitlines():
    if line.startswith("#"):
        print(" ", line)

print("\n=== SUSPICIOUS TEMPLATE TEXT ===")
for pat in ["Contoh", "Jika Ada", "isi bagian", "lorem", "TODO", "TBD", "xxx"]:
    if pat.lower() in ch.lower():
        print(" found:", pat)

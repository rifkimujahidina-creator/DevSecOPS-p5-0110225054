# Cafe Stock Manager

Aplikasi Python sederhana untuk membantu kafe mencatat bahan baku, memperbarui stok, menampilkan bahan yang perlu di-restock, dan memvalidasi data menu.

## Teknologi
- Python 3.12+
- `unittest` untuk pengujian otomatis
- Bandit sebagai Static Application Security Testing (SAST)
- GitHub Actions untuk CI

## Fitur
- Menambahkan bahan beserta batas stok minimum.
- Menambah/mengurangi stok dengan validasi agar stok tidak negatif.
- Menampilkan peringatan bahan yang mencapai batas minimum.
- Memvalidasi nama dan harga menu.
- Menampilkan laporan stok di terminal.

## Cara menjalankan
```bash
python app.py
```

Jalankan unit test:
```bash
python -m unittest discover -s tests -v
```

Jalankan SAST secara lokal:
```bash
python -m pip install bandit
bandit -r . -c bandit.yaml -ll
```

## Overview pipeline DevSecOps
Workflow `.github/workflows/devsecops.yml` terpicu pada `push` ke branch `main` dan `pull_request` yang menargetkan `main`. Job `build` memasang dependency, melakukan compile check, dan menjalankan unit test. Job `sast-scan` hanya berjalan setelah `build` berhasil (`needs: build`), kemudian menjalankan Bandit. Opsi `-ll` membuat Bandit melaporkan temuan minimal tingkat medium; temuan yang memenuhi ambang tersebut membuat job gagal dan berfungsi sebagai Quality Gate awal.

## Batasan
Bandit memeriksa pola keamanan statis Python, bukan seluruh risiko aplikasi. Quality Gate ini berbasis severity Bandit, bukan Quality Gate SonarQube. Untuk mengharuskan PR lulus sebelum merge, aktifkan branch protection/ruleset pada GitHub dan wajibkan status check `SAST Scan and Quality Gate`.

## Repository
Setelah repository dibuat, tambahkan tautan repository publik di laporan tugas.

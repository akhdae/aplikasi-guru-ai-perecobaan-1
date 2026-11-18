# PKBM DARUL HIKAM - Sistem Administrasi Guru Digital & AI

Aplikasi Administrasi Guru Digital dan PKBM terintegrasi dengan Google Gemini AI, Firebase Firestore Database, dan ekspor dokumen pembelajaran lengkap (RPP, Modul Ajar Deep Learning, Silabus, LKPD, Soal Ujian, Leger Nilai, Absensi Berbasis QR Code, dan Kalender Akademik).

---

## 🚀 Fitur Utama

1. **Dashboard & Manajemen Data**:
   - Data Siswa & Generate Cetak Kartu QR Code / Barcode Absensi
   - Manajemen Mata Pelajaran, Jadwal Mengajar, dan Kalender Akademik
   - Input Absensi Kamera Scanner QR & Rekap Kehadiran
   - Penilaian Formatif & Sumatif, Leger Nilai Otomatis
   - Jurnal & Agenda Mengajar Harian
   - Bimbingan & Konseling Guru Wali

2. **Perangkat Ajar & AI Generator Terpadu**:
   - Modul Ajar Deep Learning (Kurikulum Merdeka)
   - Generator Modul Kokurikuler Lintas Mata Pelajaran
   - Generator LKPD Interaktif & HOTS
   - Generator Soal Ujian + Lembar Jawaban Siswa (LJS) + Rubrik Kunci Jawaban
   - Generator Presentasi Pembelajaran (PPTX) otomatis dengan visual 16:9
   - Asisten Guru AI (Konsultasi Pedagogis & Administrasi)
   - Pusat Download Perangkat Ajar Lengkap (CP, TP, ATP, Prota, Prosem, KKTP)

3. **Pusat Laporan & Cetak Dokumen**:
   - Cetak Rekap Absensi Bulanan/Semester ke PDF & Excel
   - Cetak Leger Nilai & Rapor Sementara
   - Cetak Jurnal Agenda Mengajar
   - Kustomisasi Kop Surat, Logo Sekolah, dan Tanda Tangan Resmi

---

## 🛠️ Panduan Menjalankan di Komputer Lokal

### 1. Prasyarat Sistem
- **Node.js** versi 18 ke atas (direkomendasikan Node.js 20 atau 22 LTS).
- **npm** (biasanya terpasang otomatis bersama Node.js) atau **bun** / **yarn** / **pnpm**.

### 2. Langkah Instalasi

1. **Ekstrak File ZIP**:
   Ekstrak file arsip source code ke direktori pilihan Anda.

2. **Buka Terminal / Command Prompt**:
   Masuk ke folder proyek:
   ```bash
   cd pkbm-darul-hikam
   ```

3. **Install Dependensi**:
   ```bash
   npm install
   ```

4. **Konfigurasi Environment (.env)**:
   Salin file `.env.example` menjadi `.env`:
   ```bash
   cp .env.example .env
   ```
   Buka file `.env` dan masukkan API Key:
   - `GEMINI_API_KEY`: API Key dari Google AI Studio ([https://aistudio.google.com/](https://aistudio.google.com/)).
   - `AUTH_USERNAME`: Username admin login aplikasi (default: `www.yefriharyanto.id`).
   - `AUTH_PASSWORD`: Password admin login (default: `123456`).

5. **Jalankan Aplikasi dalam Mode Pengembangan**:
   ```bash
   npm run dev
   ```
   Aplikasi akan berjalan pada:
   👉 **http://localhost:3000**

6. **Build untuk Produksi**:
   ```bash
   npm run build
   npm start
   ```

---

## 📂 Struktur Direktori Proyek

```
pkbm-darul-hikam/
├── src/
│   ├── components/            # Komponen tampilan antarmuka (View)
│   │   ├── DashboardView.tsx
│   │   ├── KelolaSiswaView.tsx
│   │   ├── CetakKartuQRView.tsx
│   │   ├── InputAbsensiView.tsx
│   │   ├── ModulAjarAIView.tsx
│   │   ├── AsistenGuruAIView.tsx
│   │   ├── GeneratorSoalAIView.tsx
│   │   ├── PengaturanView.tsx
│   │   └── ...
│   ├── lib/                   # Utilitas Firebase & SweetAlert2
│   │   ├── firebase.ts
│   │   └── swal.ts
│   ├── App.tsx                # Komponen utama navigasi & state
│   ├── types.ts               # Definisi tipe data TypeScript
│   ├── main.tsx               # Entry point React
│   └── index.css              # Global styling & Tailwind CSS
├── server.ts                  # Backend Express proxy & endpoint Gemini AI
├── vite.config.ts             # Konfigurasi bundler Vite
├── package.json               # Daftar paket dependensi
├── tsconfig.json              # Konfigurasi TypeScript
├── firestore.rules            # Aturan keamanan database Firestore
└── .env.example               # Contoh konfigurasi variabel lingkungan
```

---

## 🔒 Keamanan & Lisensi
Hak Cipta © 2026 PKBM DARUL HIKAM & EdAdmin Pro. Seluruh hak cipta dilindungi.

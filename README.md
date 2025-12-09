# 🚀 ProductiBot - AI Productivity Assistant

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Gemini](https://img.shields.io/badge/Google_Gemini-8E75B2?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)

**Final Project - LLM-Based Tools and Gemini API Integration for Data Scientists**

ProductiBot adalah chatbot AI berbasis Google Gemini yang dirancang untuk membantu meningkatkan produktivitas pengguna melalui task management, time management tips, dan goal setting assistance.

---

## 📋 Table of Contents

- [Fitur Utama](#-fitur-utama)
- [Use Case](#-use-case)
- [Teknologi](#-teknologi)
- [Instalasi](#-instalasi)
- [Cara Penggunaan](#-cara-penggunaan)
- [Konfigurasi Parameter](#-konfigurasi-parameter)
- [Struktur Project](#-struktur-project)
- [Screenshots](#-screenshots)

---

## ✨ Fitur Utama

### 1. 🤖 AI-Powered Chatbot
- Menggunakan Google Gemini Pro untuk pemrosesan bahasa alami
- Memahami konteks percakapan dengan memory
- Gaya bahasa friendly dan motivational

### 2. 📝 Task Management
- Auto-detect task dari percakapan
- Tracking task dengan status
- Export task ke JSON

### 3. ⏰ Time Management
- Tips manajemen waktu
- Teknik Pomodoro
- Time blocking strategies

### 4. 🎯 Goal Setting
- Framework SMART goals
- Progress tracking
- Action plans

### 5. 📊 Analytics & Stats
- Conversation count
- Task statistics
- Session tracking

### 6. 💾 Data Persistence
- Export chat history
- Save conversations
- Task export

---

## 🎯 Use Case

**Personal Productivity Assistant** - Chatbot ini ditujukan untuk:

- **Mahasiswa**: Mengatur tugas kuliah, deadline, dan jadwal belajar
- **Pekerja**: Manajemen proyek, prioritas task, dan time management
- **Freelancer**: Goal setting, productivity tips, dan self-management
- **Semua orang**: Yang ingin meningkatkan produktivitas sehari-hari

### Contoh Penggunaan:

```
User: "Saya punya deadline project besok, tapi belum mulai. Gimana cara ngaturnya?"

ProductiBot: "Saya mengerti situasinya! Mari kita breakdown dengan teknik ini:

1. ⏰ Time Blocking (Sisa waktu: ~12 jam kerja)
   - Bagi project jadi 3-4 bagian kecil
   - Alokasi 2-3 jam per bagian
   
2. 🍅 Pomodoro Technique
   - 25 menit fokus kerja
   - 5 menit break
   - Setelah 4 sesi, break 15-30 menit

3. 📝 Prioritas:
   - Identifikasi bagian PALING PENTING dulu
   - Kerjakan yang bernilai tinggi terlebih dahulu

Mau saya bantu breakdown projectnya lebih detail?"
```

---

## 🛠 Teknologi

- **Frontend**: Streamlit (Python web framework)
- **AI Model**: Google Gemini Pro (gemini-pro)
- **Language**: Python 3.8+
- **API**: Google Generative AI API

### Parameter Konfigurasi:

| Parameter | Default | Range | Fungsi |
|-----------|---------|-------|--------|
| Temperature | 0.7 | 0.0 - 2.0 | Mengatur kreativitas response |
| Max Tokens | 1000 | 100 - 2000 | Panjang maksimal response |
| Top P | 0.95 | 0.0 - 1.0 | Nucleus sampling threshold |

---

## 🚀 Instalasi

### Prerequisites

- Python 3.8 atau lebih tinggi
- Google Gemini API Key ([Dapatkan di sini](https://makersuite.google.com/app/apikey))

### Langkah-langkah:

1. **Clone repository**
```bash
git clone https://github.com/OfelliaMA/productibot.git
cd productibot
```

2. **Buat virtual environment** (recommended)
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Setup API Key** (Optional - bisa input via UI)
```bash
cp .env.example .env
# Edit .env dan masukkan API key Anda
```

5. **Run aplikasi**
```bash
streamlit run app.py
```

6. **Buka browser**
```
http://localhost:8501
```

---

## 📖 Cara Penggunaan

### 1. Konfigurasi Awal
- Masukkan Google Gemini API Key di sidebar
- Sesuaikan parameter (temperature, max tokens, top p) sesuai kebutuhan

### 2. Mulai Chat
- Ketik pertanyaan atau permintaan di chat input
- ProductiBot akan merespons dengan saran dan tips produktivitas

### 3. Contoh Prompt:

**Task Management:**
```
"Tolong bantu saya organize tasks untuk minggu ini"
"Saya punya 5 deadline, mana yang harus diprioritaskan?"
```

**Time Management:**
```
"Bagaimana cara efektif mengatur waktu untuk belajar?"
"Apa itu teknik Pomodoro?"
```

**Goal Setting:**
```
"Saya ingin meningkatkan skill programming dalam 3 bulan"
"Buatkan goal SMART untuk karir saya"
```

**Motivasi:**
```
"Saya merasa overwhelmed dengan banyak tugas"
"Bagaimana cara tetap produktif saat mood down?"
```

### 4. Fitur Tambahan
- **View Tasks**: Lihat semua task yang sudah dibuat
- **Clear Chat**: Hapus riwayat chat
- **Export Chat**: Download percakapan dalam format JSON

---

## ⚙️ Konfigurasi Parameter

### Temperature (Creativity)
- **0.0 - 0.3**: Response sangat konsisten dan faktual
- **0.4 - 0.7**: Seimbang antara konsisten dan kreatif (Recommended)
- **0.8 - 1.5**: Lebih kreatif dan variatif
- **1.6 - 2.0**: Sangat kreatif, bisa unpredictable

### Max Tokens
- Mengatur panjang maksimal response
- **100-500**: Response singkat
- **500-1000**: Response medium (Recommended)
- **1000-2000**: Response panjang dan detail

### Top P (Nucleus Sampling)
- Mengatur diversity dari response
- **0.90-0.95**: Balanced (Recommended)
- **0.95-1.0**: Lebih diverse

---

## 📁 Struktur Project

```
productibot/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── env.txt                # API key
├── README.md              # Project documentation
│
├── screenshot/               # Screenshot
│   └── UI chatbot ProductiBot.png
│
└── exports/              # Folder untuk exported chats
    └── .gitkeep
```

---

## 📸 Screenshots

### Homepage & Configuration
![Homepage](screenshot/UI chatbot ProductiBot.png)

---

## 🔑 Mendapatkan Gemini API Key

1. Kunjungi [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Login dengan akun Google
3. Klik "Create API Key"
4. Copy API key yang dihasilkan
5. Paste ke aplikasi atau simpan di `.env`

**Note**: API key gratis dengan quota terbatas

---

## 💡 Tips Penggunaan

1. **Specific Questions**: Ajukan pertanyaan yang spesifik untuk jawaban lebih baik
2. **Context**: Berikan konteks situasi Anda untuk saran yang lebih relevan
3. **Follow-up**: Lanjutkan percakapan untuk mendapat detail lebih
4. **Experiment**: Coba berbagai parameter untuk hasil optimal
5. **Export Regularly**: Simpan percakapan penting dengan fitur export

---

## 🐛 Troubleshooting

### Error: "Invalid API Key"
- Pastikan API key benar dan aktif
- Check quota API key Anda
- Generate API key baru jika perlu

### Error: "Module not found"
- Pastikan semua dependencies terinstall: `pip install -r requirements.txt`
- Gunakan virtual environment

### Aplikasi Lambat
- Kurangi max_tokens
- Check koneksi internet
- Restart aplikasi

---

## 📝 TODO / Future Improvements

- [ ] Integration dengan Google Calendar
- [ ] Voice input/output
- [ ] Multi-language support
- [ ] Task reminder notifications
- [ ] Mobile responsive design
- [ ] Database untuk persistent storage
- [ ] User authentication
- [ ] Collaborative features

---

## 👨‍💻 Developer

**Ofellia Marvella Amin**
- GitHub: [@OfelliaM](https://github.com/OfelliaM)
- Email: ofelliamarvella@example.com

---

## 🙏 Acknowledgments

- Google Gemini API
- Streamlit Community
- Course Instructor

---

**Built with ❤️ for Final Project - LLM-Based Tools and Gemini API Integration**
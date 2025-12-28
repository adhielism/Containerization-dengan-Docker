# Aplikasi To-Do List dengan Docker

Proyek akhir mata kuliah Sistem Operasi - Implementasi containerization menggunakan Docker dengan pembatasan resource menggunakan cgroups.

## Tentang Project

Project ini adalah tugas akhir mata kuliah Sistem Operasi yang mengimplementasikan teknologi containerization menggunakan Docker. Aplikasi ini terdiri dari 2 service:

1. **Todo-App** - Aplikasi untuk mengelola daftar tugas (buat, baca, update, hapus) yang berjalan di port 5000
2. **Stats-App** - Aplikasi untuk menampilkan statistik dan analisis tugas yang berjalan di port 5001

## Fitur

- Arsitektur microservices dalam container
- Orchestration multi-container menggunakan Docker Compose
- Pembatasan resource CPU dan Memory dengan cgroups
- Komunikasi antar container melalui Docker network
- API REST untuk akses data
- Monitoring resource secara real-time

## Teknologi yang Digunakan

- **Backend**: Python 3.9 dengan Flask
- **Containerization**: Docker dan Docker Compose v2
- **Resource Management**: Linux Cgroups
- **Platform**: Docker Desktop di Windows

## Cara Menjalankan

### Kebutuhan Sistem
- Docker Desktop sudah terinstal
- Docker Compose versi 2 atau lebih baru

### Langkah-Langkah

1. Clone repository ini:
```bash
git clone https://github.com/adhielism/Containerization-dengan-Docker.git
cd Containerization-dengan-Docker
```

2. Jalankan container:
```bash
docker compose up --build
```

3. Akses aplikasi melalui browser atau curl:
- Todo App: http://localhost:5000/todos
- Stats App: http://localhost:5001/stats

4. Untuk menghentikan container:
```bash
docker compose down
```

## Konfigurasi Resource Limits

### Container Todo-App
- **Batas CPU**: 0.5 core (maksimal 50%)
- **Batas Memory**: 128 MB
- **CPU Minimum**: 0.25 core (25%)
- **Memory Minimum**: 64 MB

### Container Stats-App
- **Batas CPU**: 0.3 core (maksimal 30%)
- **Batas Memory**: 64 MB
- **CPU Minimum**: 0.15 core (15%)
- **Memory Minimum**: 32 MB

## Testing dan Monitoring

### Menguji Endpoint
```bash
# Test todo-app
curl http://localhost:5000/todos

# Test stats-app
curl http://localhost:5001/stats
```

### Monitoring Resource
```bash
# Monitoring real-time
docker stats

# Cek resource limits
docker inspect todo-app --format='{{.HostConfig.Memory}}'
docker inspect stats-app --format='{{.HostConfig.NanoCpus}}'
```

### Load Testing
```bash
# Load test untuk todo-app (di PowerShell)
for ($i=1; $i -le 20; $i++) { 
    curl http://localhost:5000/todos -UseBasicParsing
    Start-Sleep -Milliseconds 100
}
```

## Informasi Kelompok

### Anggota Kelompok
1. ADHIE MULIA SEMBIRING (2401020165)
2. MISYE KHALINA APRILIA MARBUN (2401020147)
3. RENDA KURNIA MANIK (2301020003)
4. YUDHA EKAPUTRA (2301020019)

### Detail Perkuliahan
- **Mata Kuliah**: Sistem Operasi
- **Project**: Proyek 6 - Containerization dengan Docker
- **Dosen**: Ferdi Chahyadi, S.Kom., M.Cs
- **Institusi**: Universitas Maritim Raja Ali Haji
- **Program Studi**: Teknik Informatika
- **Tahun**: 2025

## Pembelajaran

Melalui project ini, kelompok kami mempelajari:
- Konsep containerization dan perbedaannya dengan virtualisasi
- Cara membuat Docker image dan orchestration container
- Manajemen resource menggunakan Linux cgroups
- Networking multi-container dan komunikasi antar service
- Monitoring dan optimasi penggunaan resource
- Best practice deployment aplikasi berbasis container

## Lisensi


Project ini dibuat untuk memenuhi tugas akhir mata kuliah Sistem Operasi.

# 🔥 Zip2Git — Upload ZIP Langsung ke GitHub

**Zip2Git** adalah tools berbasis Python untuk Termux yang bisa:
- 📦 mengekstrak file `.zip` otomatis  
- ☁️ mengupload seluruh isi file ke repository GitHub  
- 💾 menyimpan token & nama repo agar tidak perlu input berulang  


## ⚙️ Persiapan Awal

### 1️⃣ Instalasi di Termux
```bash
pkg install python git -y
pip install requests
````

clone atau buat folder project Zip2Git:

```bash
git clone https://github.com/frhndevweb/Zip2Git
cd Zip2Git
```


### 2️⃣ Ganti Repo dan Token di `config.json`

Buka file `config.json` lalu ubah jadi seperti ini:

```json
{
    "repo": "username/nama-repo",
    "token": "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}
```

> 💡 **Keterangan:**
>
> * `repo` = nama repository di GitHub (contoh: `frhndevweb/zip-upload-test`)
> * `token` = Personal Access Token (PAT) dari akun GitHub lo


## 🚀 Cara Menggunakan Zip2Git

### 1️⃣ Siapkan file ZIP

Pastikan file ZIP lo udah ada di Termux. Misal:

```
/storage/emulated/0/Documents/G01-ST-Pro.zip
```

Kalau belum bisa diakses, aktifkan izin storage:

```bash
termux-setup-storage
```


### 2️⃣ Jalankan Tools

```bash
python zip2git.py
```


### 3️⃣ Tunggu Proses Upload

Tools akan:

1. Mengekstrak file ZIP ke folder `temp_extract`
2. Upload semua isi ke GitHub lewat API
3. Menghapus folder sementara setelah selesai

Output berhasil:

```
[+] Uploaded: index.html
[+] Uploaded: style.css
[+] Uploaded: script.js
[✅] Upload selesai!
```


## 🧠 Langkah Membuat Repo & Token GitHub

### 🔹 Membuat Repository

1. Buka [GitHub.com](https://github.com/)
2. Klik tombol **New repository**
3. Isi nama repo (contoh: `zip-upload-test`)
4. **Jangan centang** “Add README” (boleh bikin manual nanti)
5. Klik **Create repository**
6. Format repo untuk `config.json` → `username/zip-upload-test`


### 🔹 Membuat Personal Access Token (PAT)

1. Buka [Settings → Developer settings → Tokens (classic)](https://github.com/settings/tokens)
2. Klik **Generate new token (classic)**
3. Centang scope:

   * ✅ `repo`
   * ✅ `workflow` *(opsional tapi disarankan)*
4. Klik **Generate token**
5. Copy token-nya dan simpan (muncul cuma sekali!)

Contoh format token:

```
ghp_4XrLx7f5GQ1tXq2W3aBcD9efg0hYpK6mNnP
```


## 🧰 Tips Tambahan

* Gunakan **repo kosong** dengan branch `main` aktif
* Jangan upload file ZIP lebih besar dari 20 MB per file
* Simpan token di tempat aman, karena punya akses penuh ke repo lo
* Kalau mau ganti token / repo → ubah aja langsung di `config.json`


💡 **Contoh Lengkap `config.json`**

```
{
    "repo": "frhndevweb/zip-upload-test",
    "token": "ghp_4XrLx7f5GQ1tXq2W3aBcD9efg0hYpK6mNnP"
}
```


🎉 **Sekarang lo bisa upload project .zip langsung dari Termux ke GitHub tanpa repot extract manual!**

```
python zip2git.py
```

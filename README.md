# Aplikasi REST API Produk

Project ini adalah aplikasi web sederhana untuk mengelola data produk menggunakan Flask dan SQLite (sebagai database).

## Fitur

- Create (Tambah Produk)
- Read (Menampilkan Produk)
- Update (Mengubah Produk)
- Delete (Menghapus Produk)

## Teknologi

- Python (bahasa pemrograman utama)
- Flask (Framework backend/API)
- SQLite (database)
- Flask SQLAlchemy (penghubung flask dengan database)
- HTML (tampilan UI/frontend)
- JavaScript (frontend dengan API)
  
## Endpoint API

| Method | Endpoint | Fungsi |
|---|---|---|
| GET ALL | /api/produk |Menampilkan semua produk
| GET BY ID | /api/produk/<id> | Menampilkan satu produk berdasarkan id |
| POST | /api/produk | Menambah produk |
| PUT BY ID | /api/produk/<id> | Mengubah produk berdasarkan ID |
| DELETE | /api/produk/<id> | Menghapus produk |

## Cara Menjalankan

```bash
py app.py
```

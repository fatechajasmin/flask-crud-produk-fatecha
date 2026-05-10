from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy

# Membuat aplikasi Flask
app = Flask(__name__)

# Menghubungkan database SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///produk.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Membuat tabel produk
class Produk(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    harga = db.Column(db.Integer, nullable=False)

# Membuat database jika belum ada
with app.app_context():
    db.create_all()

# HOME
@app.route('/')
def home():
    return render_template('index.html')

# READ
# Menampilkan semua produk
@app.route('/api/produk', methods=['GET'])
def get_produk():
    semua_produk = Produk.query.all()

    hasil = []
    for p in semua_produk:
        hasil.append({
            "id": p.id,
            "nama": p.nama,
            "harga": p.harga
        })

    return jsonify(hasil)

# GET BY ID
# Menampilkan satu produk berdasarkan id
@app.route('/api/produk/<int:id>', methods=['GET'])
def get_produk_by_id(id):
    produk = Produk.query.get(id)

    if produk is None:
        return jsonify({"message": "produk tidak ditemukan"}), 404

    return jsonify({
        "id": produk.id,
        "nama": produk.nama,
        "harga": produk.harga
    })

# CREATE
# Menambahkan produk baru ke database
@app.route('/api/produk', methods=['POST'])
def tambah_produk():
    data = request.json

    if not data or "nama" not in data or "harga" not in data:
        return jsonify({"message": "nama dan harga wajib diisi"}), 400

    produk_baru = Produk(
        nama=data["nama"],
        harga=data["harga"]
    )

    db.session.add(produk_baru)
    db.session.commit()

    return jsonify({
        "message": "produk berhasil ditambah",
        "data": {
            "id": produk_baru.id,
            "nama": produk_baru.nama,
            "harga": produk_baru.harga
        }
    }), 201

# UPDATE
# Mengubah data produk berdasarkan id
@app.route('/api/produk/<int:id>', methods=['PUT'])
def update_produk(id):
    produk = Produk.query.get(id)

    if produk is None:
        return jsonify({"message": "produk tidak ditemukan"}), 404

    data = request.json

    if not data or "nama" not in data or "harga" not in data:
        return jsonify({"message": "nama dan harga wajib diisi"}), 400

    produk.nama = data["nama"]
    produk.harga = data["harga"]

    db.session.commit()

    return jsonify({
        "message": "produk berhasil diupdate",
        "data": {
            "id": produk.id,
            "nama": produk.nama,
            "harga": produk.harga
        }
    })

# DELETE
# Menghapus produk berdasarkan id
@app.route('/api/produk/<int:id>', methods=['DELETE'])
def hapus_produk(id):
    produk = Produk.query.get(id)

    if produk is None:
        return jsonify({"message": "produk tidak ditemukan"}), 404

    db.session.delete(produk)
    db.session.commit()

    return jsonify({
        "message": f"produk dengan id {id} berhasil dihapus"
    })

# Menjalankan server Flask
if __name__ == '__main__':
    app.run(debug=True)
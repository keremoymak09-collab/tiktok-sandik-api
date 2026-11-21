from flask import Flask, request, jsonify
import os
import time

app = Flask(__name__)

son_sandik = {}

@app.route("/")
def ana():
    return jsonify({
        "durum": "aktif",
        "proje": "TikTok Sandık Bulucu API"
    })

@app.route("/sandik", methods=["GET"])
def sandik_getir():
    return jsonify(son_sandik)

@app.route("/sandik", methods=["POST"])
def sandik_ekle():
    global son_sandik

    anahtar = os.environ.get("API_KEY")
    gelen = request.headers.get("X-API-Key")

    if not anahtar or gelen != anahtar:
        return jsonify({"hata": "Yetkisiz erişim"}), 401

    veri = request.get_json(silent=True)

    if not isinstance(veri, dict):
        return jsonify({"hata": "Geçersiz veri"}), 400

    son_sandik = veri
    son_sandik["kayit_zamani"] = int(time.time())

    return jsonify({"durum": "kaydedildi"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

import kbb

def handler(request):
    # Panggil fungsi atau proses dari kbb.py
    # Kalau cuma pengujian, balas simple saja
    return {
        "statusCode": 200,
        "body": "Server berjalan dengan baik!"
    }
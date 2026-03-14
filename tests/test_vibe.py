import requests
payload = {"motoboy": "Wendell_01", "pacote": "PACK-VIBE-2026", "status": "EM DESLOCAMENTO"}
try:
    r = requests.post("http://127.0.0.1:5000/status", json=payload)
    print(f"Resultado: {r.status_code} - {r.json()['notificacao']}")
except Exception as e:
    print(f"❌ Erro: {e}")

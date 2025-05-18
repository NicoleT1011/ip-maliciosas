
import whois

# Esta funcion obtiene informacion WHOIS de la IP usando python

def show_whois(ip):
    try:
        w = whois.whois(ip)
        print(f"[WHOIS] Información de {ip}:\n")
        for k, v in w.items():
            print(f"{k}: {v}")
    except Exception as e:
        print(f"[ERROR] No se pudo obtener WHOIS: {e}")

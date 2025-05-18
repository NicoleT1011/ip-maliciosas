import whois

def consulta_whois(dominio):
    """
    Realiza una consulta WHOIS simple para un dominio o IP.
    
    Parámetros:
        dominio (str): Dominio o IP a consultar.
        
    Retorna:
        dict: Información WHOIS relevante o mensaje de error.
    """
    try:
        resultado = whois.whois(dominio)
        
        # Para evitar errores al convertir resultado a dict, convertimos solo algunos campos
        info = {
            "domain_name": resultado.domain_name,
            "registrar": resultado.registrar,
            "whois_server": resultado.whois_server,
            "creation_date": str(resultado.creation_date),
            "expiration_date": str(resultado.expiration_date),
            "name_servers": resultado.name_servers,
            "status": resultado.status,
            "emails": resultado.emails
        }
        return info
    except Exception as e:
        return {"error": f"No se pudo obtener WHOIS: {e}"}

# Ejemplo de uso
if __name__ == "__main__":
    dominio_test = "example.com"
    resultado = consulta_whois(dominio_test)
    print(resultado)

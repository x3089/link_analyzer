import requests
import re
import sys

def print_banner():
    banner = """
 █████  ███████ ████████ ██████   █████  
██   ██ ██         ██    ██   ██ ██   ██ 
███████ ███████    ██    ██████  ███████ 
██   ██      ██    ██    ██   ██ ██   ██ 
██   ██ ███████    ██    ██   ██ ██   ██ 
                                         
                                         
PEGA EL LINK AQUI: (link por examinar)
    """
    print(banner)

def is_malicious(link):
    # Simple checks for common phishing or malicious indicators
    patterns = [
        r"\bfree\b",  # Contains the word 'free'
        r"\bwin\b",   # Contains the word 'win'
        r"\.exe$",    # Links ending in .exe
        r"@.*\.",     # Links containing '@' symbol
    ]
    for pattern in patterns:
        if re.search(pattern, link, re.IGNORECASE):
            return True
    return False

def analyze_link(link):
    try:
        response = requests.get(link, timeout=5)
        status_code = response.status_code
        headers = response.headers

        print("[INFO] Análisis del link:")
        print(f"- Código HTTP: {status_code}")
        print(f"- Encabezados de respuesta: {headers}")
        
        if status_code == 200:
            print("[INFO] El link es accesible. Analizando contenido...")
            if is_malicious(link):
                print("\033[91m[CRÍTICO] El link contiene posibles indicadores de phishing o virus.\033[0m")
            else:
                print("\033[92m[SEGURO] El link no parece ser malicioso basado en los patrones comunes.\033[0m")
        elif 400 <= status_code < 500:
            print("\033[93m[SOSPECHOSO] El link devolvió un código HTTP indicando un posible problema del cliente.\033[0m")
        elif 500 <= status_code < 600:
            print("\033[91m[CRÍTICO] El link devolvió un código HTTP indicando un problema del servidor.\033[0m")
        else:
            print(f"[ALERTA] El link devolvió un código HTTP inusual: {status_code}")
    except requests.exceptions.RequestException as e:
        print(f"\033[91m[ERROR] No se pudo acceder al link. Detalles: {e}\033[0m")

if __name__ == "__main__":
    print_banner()
    link = input("Pega el link aquí: ")
    analyze_link(link)

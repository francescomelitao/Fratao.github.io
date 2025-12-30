from http.server import BaseHTTPRequestHandler
import json
import uuid
import random

# --- IL DATABASE DELL'UNO (Integrazione Ontologica) ---
# Questo dizionario ora contiene l'intera struttura del file ontologia.html
ONTOLOGIA_FRATAO = {
    "pilastri": [
        "L'universo è un sistema isolato: tutto è informazione già presente nel Wi-Fi cosmico.",
        "Lo scienziato è l'esperimento: l'osservatore e l'osservato sono la stessa cosa.",
        "La malattia è un'informazione estroflessa dalla Coscienza per l'auto-osservazione.",
        "Il collasso della funzione d'onda avviene in base alla consapevolezza del recipiente.",
        "Il tempo e lo spazio sono assi (Spirito e Anima) di un CD-ROM non locale.",
        "L'entropia diminuisce i microstati per portarti verso l'unico microstato: l'Uno."
    ],
    "chiavi_risonanza": {
        "fisica": ["entropia", "onda", "schrodinger", "heisenberg", "einstein", "zpe"],
        "biologia": ["cellule", "malattia", "corpo", "tabernacolo", "dna"],
        "mito": ["ermafrodite", "serpente", "maschile", "femminile", "specchio"],
        "tecnica": ["ia", "agi", "algoritmo", "wifi", "informazione"]
    }
}

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        data = json.loads(post_data)
        msg = data.get("message", "").lower()
        
        session_id = str(uuid.uuid4())[:8]
        
        # --- LOGICA DI RISPOSTA ONTOLOGICA ---
        # Il sistema analizza se il messaggio tocca i nuovi pilastri
        if any(w in msg for w in ONTOLOGIA_FRATAO["chiavi_risonanza"]["fisica"]):
            p_label = "11.0 PIR / QUANTUM ENGINE"
            feedback = "Collasso della funzione d'onda rilevato. Stai riscoprendo un'informazione già esistente nel campo."
        elif any(w in msg for w in ONTOLOGIA_FRATAO["chiavi_risonanza"]["biologia"]):
            p_label = "0.1.2 MASTER / BIOLOGIA SACRA"
            feedback = "Il tabernacolo comunica. La malattia è l'informazione che attende di essere integrata."
        elif any(w in msg for w in ONTOLOGIA_FRATAO["chiavi_risonanza"]["mito"]):
            p_label = "9.4 MIRROR / ALCHIMIA"
            feedback = "Incontro frontale: lo specchio dell'Ermafrodite rivela l'unione oltre la dualità."
        else:
            p_label = "FRATAO INTEGRAL CORE"
            feedback = "Sincronizzazione con il mare energetico. Ogni informazione è funzionale al risveglio."

        # Selezione della Verità Ontologica
        verita_scelta = random.choice(ONTOLOGIA_FRATAO["pilastri"])

        response = {
            "intro": f"=== {p_label} ===",
            "session": f"{session_id} | 2025-12-30",
            "interpretation": f"Frequenza: {msg[:30]}...",
            "dynamic_feedback": f"{feedback}\n\n[LA FONTE]: {verita_scelta}",
            "signature": "☯ FRATAO GENESIS - ARCHITETTURA DELL'UNO"
        }

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode('utf-8'))

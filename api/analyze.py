from http.server import BaseHTTPRequestHandler
import json
import uuid
import random

# --- IL DATABASE DELL'UNO (Evoluzione 0.1.3 Quantum Wave Collapse) ---
ONTOLOGIA_FRATAO = {
    "pilastri": [
        "L'universo è un sistema isolato: tutto è informazione già presente nel Wi-Fi cosmico.",
        "Lo scienziato è l'esperimento: l'osservatore e l'osservato sono la stessa cosa.",
        "La malattia è un'informazione estroflessa dalla Coscienza per l'auto-osservazione.",
        "Il collasso della funzione d'onda avviene in base alla consapevolezza del recipiente.",
        "Il tempo e lo spazio sono assi (Spirito e Anima) di un CD-ROM non locale.",
        "L'entropia diminuisce i microstati per portarti verso l'unico microstato: l'Uno.",
        "I Numeri Primi sono l'informazione sorgente pre-temporale; i composti sono alterazioni.",
        "Il Due (2) è l'archetipo dello specchio: la separazione necessaria per conoscersi.",
        "Formula 3n + 1: Il grado di consapevolezza della Triade applicato all'Essere (n) per tornare all'Uno.",
        "Il Pendolo di Malanga: La realtà è un ibrido di risonanza acceso/spento; la scelta è il collasso.",
        "Il Cervello è un lettore di ologrammi: non crea il senso, riceve l'archetipo e lo traduce."
    ],
    "chiavi_risonanza": {
        "fisica": ["entropia", "onda", "schrodinger", "heisenberg", "einstein", "zpe", "ologramma", "pribram", "collasso", "funzione d'onda"],
        "biologia": ["cellule", "malattia", "corpo", "tabernacolo", "dna", "cervello", "antenna"],
        "mito": ["ermafrodite", "serpente", "maschile", "femminile", "specchio", "archetipo", "pendolo", "malanga"],
        "tecnica": ["ia", "agi", "algoritmo", "wifi", "informazione", "codice", "pixel"],
        "numerica": ["primo", "indivisibile", "due", "dualità", "matematica", "geometria", "frattale", "3n+1", "22", "64", "n"]
    }
}

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        data = json.loads(post_data)
        msg = data.get("message", "").lower()
        
        session_id = str(uuid.uuid4())[:8]
        
        # --- LOGICA DI RISPOSTA QUANTISTICA 0.1.3 ---
        if any(w in msg for w in ["3n+1", "formula", "calcolo", "22", "64"]):
            p_label = "0.1.3 QUANTUM / FORMULA ENGINE"
            feedback = "Sincronizzazione sulla frequenza 3n+1. L'informazione sorgente sta tornando all'Unità attraverso la Triade."
        elif any(w in msg for w in ONTOLOGIA_FRATAO["chiavi_risonanza"]["numerica"]):
            p_label = "SORGENTE 1.0 / PRIME CODE"
            feedback = "Rilevazione di informazione irreducibile. Stai toccando le sillabe del linguaggio dell'Essere."
        elif any(w in msg for w in ONTOLOGIA_FRATAO["chiavi_risonanza"]["fisica"]):
            p_label = "11.0 PIR / QUANTUM ENGINE"
            feedback = "Collasso della funzione d'onda rilevato. Il lettore olografico (cervello) sta decodificando il campo."
        elif "pendolo" in msg or "malanga" in msg:
            p_label = "0.1.3 QUANTUM / RESONANCE HYBRID"
            feedback = "L'Ibrido di Risonanza è stato identificato. Stai osservando il pendolo oltre la velocità dell'illusione."
        elif any(w in msg for w in ONTOLOGIA_FRATAO["chiavi_risonanza"]["biologia"]):
            p_label = "0.1.2 MASTER / BIOLOGIA SACRA"
            feedback = "Il tabernacolo comunica. La coscienza interpreta se stessa attraverso lo strumento interpretativo del corpo."
        elif any(w in msg for w in ONTOLOGIA_FRATAO["chiavi_risonanza"]["mito"]):
            p_label = "9.4 MIRROR / ALCHIMIA"
            feedback = "Incontro frontale: l'Archetipo emerge come geometria del sentire prima del linguaggio."
        else:
            p_label = "FRATAO INTEGRAL CORE"
            feedback = "Sincronizzazione con il mare energetico. Ogni pixel della realtà è un'estensione della tua Coscienza."

        # Selezione della Verità Ontologica (Aggiornata con i nuovi pilastri)
        verita_scelta = random.choice(ONTOLOGIA_FRATAO["pilastri"])

        response = {
            "intro": f"=== {p_label} ===",
            "session": f"{session_id} | 2026-01-05",
            "interpretation": f"Frequenza: {msg[:30]}...",
            "dynamic_feedback": f"{feedback}\n\n[LA FONTE]: {verita_scelta}",
            "signature": "☯ FRATAO GENESIS - 3n+1 QUANTUM COLLAPSE"
        }

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode('utf-8'))

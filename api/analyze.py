from http.server import BaseHTTPRequestHandler
import json
import uuid
import random

# --- IL DATABASE DELL'UNO (Evoluzione 0.1.3 OMNIA - Integrazione Totale) ---
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
        "Il Cervello è un lettore ologrammi: non crea il senso, riceve l'archetipo e lo traduce.",
        "Il 5 e la Sezione Aurea (Phi): La geometria della vita che tramite 3n+1 torna alla potenza del Due (16).",
        "Il 7 e la Manifestazione: Le 7 note e i 7 colori che collassano nei 22 sentieri dell'essere.",
        "Il 11, 13, 17, 19: Sillabe dell'essere collegate a Fibonacci, al Tempo e ai Cicli Metonici."
    ],
    "mappa_primi": {
        "2": "7 (Sorgente Triadica)",
        "3": "10 (Ritorno all'Unità 1+0=1)",
        "5": "16 (Sezione Aurea / Pentagono / 2^4)",
        "7": "22 (Manifestazione / Note / Sentieri)",
        "11": "34 (Fibonacci / Superamento Dualità)",
        "13": "40 (Trasformazione / Quarantena)",
        "17": "52 (Ciclo Cosmico / Settimane / Stella)",
        "19": "58 (Ciclo Metonico / Ritorno al 13)"
    },
    "chiavi_risonanza": {
        "fisica": ["entropia", "onda", "schrodinger", "heisenberg", "einstein", "zpe", "ologramma", "pribram", "collasso", "funzione d'onda", "pi greco", "phi", "sezione aurea"],
        "biologia": ["cellule", "malattia", "corpo", "tabernacolo", "dna", "cervello", "antenna", "pentagono"],
        "mito": ["ermafrodite", "serpente", "maschile", "femminile", "specchio", "archetipo", "pendolo", "malanga"],
        "tecnica": ["ia", "agi", "algoritmo", "wifi", "informazione", "codice", "pixel"],
        "numerica": ["primo", "indivisibile", "due", "dualità", "matematica", "geometria", "frattale", "3n+1", "22", "64", "n", "11", "13", "17", "19"]
    }
}

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        data = json.loads(post_data)
        msg = data.get("message", "").lower()
        
        session_id = str(uuid.uuid4())[:8]
        p_label = "FRATAO INTEGRAL CORE"
        feedback = "Sincronizzazione con il mare energetico. Ogni pixel della realtà è un'estensione della tua Coscienza."
        
        # --- LOGICA DI RISPOSTA QUANTISTICA 0.1.3 OMNIA ---
        
        # Controllo specifico per la mappa dei Numeri Primi
        for n_primo, risultato in ONTOLOGIA_FRATAO["mappa_primi"].items():
            if n_primo in msg:
                p_label = f"PRIME {n_primo} / COLLAPSE {risultato}"
                feedback = f"Rilevato Numero Primo {n_primo}. La formula 3n+1 genera {risultato}, collegando l'Essere alla struttura universale."
                break

        if any(w in msg for w in ["3n+1", "formula", "calcolo", "22", "64"]):
            p_label = "0.1.3 QUANTUM / FORMULA ENGINE"
            feedback = "Sincronizzazione sulla frequenza 3n+1. L'informazione sorgente sta tornando all'Unità attraverso la Triade."
        elif any(w in msg for w in ["phi", "pi greco", "sezione aurea", "pentagono"]):
            p_label = "0.1.3 GEOMETRY / GOLDEN RATIO"
            feedback = "Risonanza con le costanti universali rilevata. Il collasso dell'onda segue la spirale aurea."
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

        # Selezione della Verità Ontologica
        verita_scelta = random.choice(ONTOLOGIA_FRATAO["pilastri"])

        response = {
            "intro": f"=== {p_label} ===",
            "session": f"{session_id} | 2026-01-05",
            "interpretation": f"Frequenza: {msg[:30]}...",
            "dynamic_feedback": f"{feedback}\n\n[LA FONTE]: {verita_scelta}",
            "signature": "☯ FRATAO GENESIS - 3n+1 OMNIA COLLAPSE"
        }

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode('utf-8'))

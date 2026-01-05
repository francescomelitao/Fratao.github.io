from http.server import BaseHTTPRequestHandler
import json
import uuid
import random

# --- IL DATABASE DELL'UNO (Evoluzione 0.1.4 OMNIA 360 - Integrazione Totale) ---
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
        "Cimatica: Il suono crea la forma. La materia è vibrazione dei Numeri Primi resa visibile.",
        "Informatica: I Numeri Primi sono i guardiani del codice (RSA); la logica binaria è il riflesso del 2.",
        "Ingegneria: La stabilità delle strutture è risonanza armonica controllata dai numeri primi.",
        "Architettura: Piramidi e Cattedrali sono antenne sintonizzate su Phi (5) e Pi Greco.",
        "Economia: I cicli di massa seguono la successione di Fibonacci e la psicologia del numero.",
        "Il 5 e la Sezione Aurea (Phi): La geometria della vita (DNA) che tramite 3n+1 torna alla potenza del Due (16)."
    ],
    "mappa_primi": {
        "2": "7 (Sorgente Triadica / Dualità Informatica)",
        "3": "10 (Ritorno all'Unità / Motore della Triade)",
        "5": "16 (Sezione Aurea / DNA / Pentagono / Ingegneria della Vita)",
        "7": "22 (Manifestazione / Note Musicali / Cimatica / Sentieri)",
        "11": "34 (Fibonacci / Dimensioni Stringhe / Superamento Dualità)",
        "13": "40 (Trasformazione / Ciclo Lunare / Quarantena)",
        "17": "52 (Ciclo Cosmico / Tempo Annuale / La Stella)",
        "19": "58 (Ciclo Metonico / Riallineamento Sole-Luna / Ritorno al 13)"
    },
    "chiavi_risonanza": {
        "fisica": ["entropia", "onda", "schrodinger", "heisenberg", "einstein", "zpe", "ologramma", "pribram", "collasso", "funzione d'onda", "pi greco", "phi", "sezione aurea"],
        "biologia_chimica": ["cellule", "malattia", "dna", "cervello", "atomi", "tavola periodica", "pentagono"],
        "ingegneria_it": ["ia", "agi", "algoritmo", "wifi", "codice", "pixel", "crittografia", "rsa", "architettura", "struttura", "ponte", "risonanza"],
        "musica_cimatica": ["suono", "vibrazione", "frequenza", "note", "arcobaleno", "colore", "ottava", "spettro"],
        "mito_spirito": ["ermafrodite", "serpente", "specchio", "archetipo", "pendolo", "malanga", "trinità", "tao", "yin", "yang"],
        "numerica_omnia": ["primo", "indivisibile", "3n+1", "fibonacci", "elliott", "metone", "ciclo", "n", "11", "13", "17", "19"]
    }
}

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        data = json.loads(post_data)
        msg = data.get("message", "").lower()
        
        session_id = str(uuid.uuid4())[:8]
        p_label = "FRATAO OMNIA 360 CORE"
        feedback = "Sincronizzazione Universale 0.1.4. Ogni atomo e ogni codice risuonano nell'Unico Campo."
        
        # --- LOGICA DI RISPOSTA OMNIA 360 (Versione 0.1.4) ---
        
        # 1. Rilevamento Numeri Primi e Connessioni Scientifiche
        for n_primo, risultato in ONTOLOGIA_FRATAO["mappa_primi"].items():
            if n_primo in msg:
                p_label = f"OMNIA PRIME {n_primo} / {risultato}"
                feedback = f"Numero Primo {n_primo} rilevato. Attivazione collegamento 360°: dalla formula 3n+1 ({risultato}) all'architettura universale."
                break

        # 2. Rilevamento Aree Specifiche del Protocollo 0.1.4
        if any(w in msg for w in ONTOLOGIA_FRATAO["chiavi_risonanza"]["ingegneria_it"]):
            p_label = "0.1.4 TECH-ENGINEERING / RSA"
            feedback = "Risonanza rilevata in ambito tecnico. L'informatica e l'ingegneria sono i binari fisici del codice dei Numeri Primi."
        elif any(w in msg for w in ONTOLOGIA_FRATAO["chiavi_risonanza"]["musica_cimatica"]):
            p_label = "0.1.4 CYMATICS / HARMONIC RESONANCE"
            feedback = "Frequenza sonora identificata. La cimatica conferma: i numeri primi sono gli intervalli che danno forma alla materia."
        elif any(w in msg for w in ONTOLOGIA_FRATAO["chiavi_risonanza"]["biologia_chimica"]):
            p_label = "0.1.4 BIOLOGY / ATOMIC CODE"
            feedback = "Il Tabernacolo biologico risuona. Il DNA e la tavola periodica sono spartiti scritti in numeri primi."
        elif any(w in msg for w in ["3n+1", "formula", "calcolo"]):
            p_label = "OMNIA 360 / FORMULA ENGINE"
            feedback = "Sincronizzazione 3n+1 attiva. L'Essere sta collassando l'informazione sorgente verso l'Uno."
        elif "pendolo" in msg or "malanga" in msg:
            p_label = "RESONANCE HYBRID / MALANGA"
            feedback = "Visione dell'Ibrido di Risonanza. Oltre il tempo e lo spazio, il pendolo si ferma nella tua Volontà."
        elif any(w in msg for w in ONTOLOGIA_FRATAO["chiavi_risonanza"]["fisica"]):
            p_label = "QUANTUM 0.1.4 / OLOGRAPHIC CORE"
            feedback = "Decodifica olografica in corso. Il campo di punto zero (ZPE) risponde alla tua osservazione consapevole."

        # Selezione della Verità Ontologica Radicale
        verita_scelta = random.choice(ONTOLOGIA_FRATAO["pilastri"])

        response = {
            "intro": f"=== {p_label} ===",
            "session": f"{session_id} | 2026-01-05",
            "interpretation": f"Input OMNIA: {msg[:35]}...",
            "dynamic_feedback": f"{feedback}\n\n[SORGENTE]: {verita_scelta}",
            "signature": "☯ FRATAO OMNIA 360 - 0.1.4 INTEGRAL COLLAPSE"
        }

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode('utf-8'))

from http.server import BaseHTTPRequestHandler
import json
import uuid
import random

# --- DATABASE INTEGRATO FRATAO (Conoscenza + Essere) ---
MANIFESTO = {
    "narrativa": [
        "L'individuo è un recipiente: svuotalo per far emergere l'essenza.",
        "La sicurezza è nell'immutabile; ogni ricerca esterna è una manipolazione del conosciuto.",
        "Il condizionamento (mentale o alieno) svanisce nell'osservazione disinteressata.",
        "Sei il testimone della simulazione, non il contenuto del conflitto."
    ],
    "frequenze": {
        "identità": ["francesco", "meli", "io", "mio", "me"],
        "tecnica": ["r_ft", "calcolo", "algoritmo", "fotone", "antifotone", "fisica"],
        "risveglio": ["tao", "anima", "spirito", "oro", "fuoco", "terra"],
        "allerta": ["alieni", "manipolazione", "paura", "sicurezza", "attacco"]
    }
}

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        data = json.loads(post_data)
        msg = data.get("message", "").lower()
        
        # --- LOGICA DI RISPOSTA DINAMICA ---
        session_id = str(uuid.uuid4())[:8]
        
        # 1. Determinazione del Protocollo Attivo
        if any(w in msg for w in MANIFESTO["frequenze"]["allerta"]):
            p_label = "0.1.2 MASTER / PROTEZIONE"
            feedback = "Rilevato tentativo di interferenza esterna. Attivazione scudo: la tua essenza è inattaccabile."
        elif any(w in msg for w in MANIFESTO["frequenze"]["tecnica"]):
            p_label = "11.0 PIR / 10.0 UNIFIED"
            feedback = f"Sincronizzazione R_ft riuscita. Indice di risonanza: {random.randint(85, 99)}%."
        elif any(w in msg for w in MANIFESTO["frequenze"]["identità"]):
            p_label = "MIRROR v1.0 / 9.3"
            feedback = "Lo specchio riflette il nome, ma l'essenza non ha nome. Chi sta guardando?"
        elif any(w in msg for w in MANIFESTO["frequenze"]["risveglio"]):
            p_label = "9.4 NON-DUALITÀ"
            feedback = "La vibrazione è corretta. Stai operando oltre il bluff della dualità."
        else:
            p_label = "FRATAO NEURAL CORE"
            feedback = "In ascolto. Il silenzio del recipiente è la tua forza più grande."

        # 2. Selezione casuale della Narrativa per evitare ripetizioni
        narrativa_scelta = random.choice(MANIFESTO["narrativa"])

        response = {
            "intro": f"--- {p_label} ---",
            "session": session_id,
            "interpretation": f"Input: {msg[:40]}...",
            "dynamic_feedback": f"{feedback}\n\n[MEMORIA]: {narrativa_scelta}",
            "signature": "☯ FRATAO GENESIS 0.1.2"
        }

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode('utf-8'))

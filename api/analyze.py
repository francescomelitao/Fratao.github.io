from http.server import BaseHTTPRequestHandler
import json
import uuid

# INTEGRAZIONE MANIFESTO FRA TAO 0.1.2 FURE GENESIS MASTER
# Include la Narrativa della Coscienza per la verifica della simulazione
MANIFESTO_INTEGRALE = {
    "narrativa_coscienza": "L'individuo è un recipiente condizionato dal passato. La sicurezza non esiste esternamente (alieni/manipolazioni), ma nell'essenza immutabile.",
    "protocolli": {
        "9.3": "Rigore e Wu Wei - Svuotamento del conosciuto.",
        "10.0": "Unified Engine - Metriche SDA e rilascio consapevole.",
        "11.0": "PIR - Risonanza Ignition ed equazione R_ft.",
        "Mirror": "Riflesso puro senza giudizio - Non-intervento."
    },
    "parole_chiave": ["Anima", "Spirito", "Terra", "Oro", "Fuoco", "Antifotone"]
}

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)
        message = data.get("message", "").lower()

        # LOGICA DI INTEGRAZIONE (Conoscenza + Essere)
        session_id = str(uuid.uuid4())[:13]
        
        # Selezione dinamica del protocollo in base al messaggio
        if "specchio" in message or "conflitto" in message:
            p_active = "Mirror v1.0"
            feedback = "Riflesso attivo: osserva il condizionamento senza intervenire."
        elif "energia" in message or "fisica" in message:
            p_active = "11.0 PIR"
            feedback = "Innesco Risonanza R_ft: calcolo antifotoni in corso."
        else:
            p_active = "0.1.2 Genesis Master"
            feedback = "Sincronizzazione con l'essenza immutabile di Francesco Meli."

        response = {
            "intro": f"=== FRATAO UNIFIED ENGINE (Tutti i Protocolli Attivi) ===",
            "session": session_id,
            "interpretation": f"Analisi Multidimensionale: {message}",
            "active_protocol": p_active,
            "dynamic_feedback": f"{feedback}\n\nNota dalla Coscienza: {MANIFESTO_INTEGRALE['narrativa_coscienza']}",
            "signature": "☯"
        }

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode('utf-8'))

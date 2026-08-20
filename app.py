from flask import Flask, request, jsonify
from datetime import datetime, timezone
import json
import os

app = Flask(__name__)

# File to store incoming webhooks
LOG_FILE = "webhook_logs.json"

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "active", "message": "Webhook receiver is running!"}), 200

@app.route("/webhook", methods=["POST"])
def receive_webhook():
    # Parse incoming JSON payload
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "No JSON payload received"}), 400

    # Attach server timestamp
    log_entry = {
        "received_at": datetime.now(timezone.utc).isoformat(),
        "payload": data
    }

    # Save to local log file
    logs = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            try:
                logs = json.load(f)
            except json.JSONDecodeError:
                logs = []
                
    logs.append(log_entry)
    
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)

    print(f"\n[WEBHOOK RECEIVED] Payload: {data}\n")

    return jsonify({"status": "success", "message": "Webhook payload logged"}), 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)
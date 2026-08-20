# Meridian Pivot — Webhook Prototype

Solo Day 1-2 webhook mini-prototype — Meridian Pivot sprint.. This is a lightweight Flask-based webhook receiver built as part of the Meridian Pivot sprint (Solo Day 1–2). This prototype demonstrates how to receive, process, and log incoming HTTP `POST` webhook payloads.

## Features

* Exposes a `/webhook` endpoint listening for incoming `POST` requests.
* Validates incoming JSON payloads and attaches a server-side timestamp.
* Persists logged webhook payloads locally in `webhook_logs.json`.
* Includes a primary health-check route at `/`.

## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Wycliffe-M/meridian-pivot-webhook-prototype.git](https://github.com/Wycliffe-M/meridian-pivot-webhook-prototype.git)
   cd meridian-pivot-webhook-prototype

2. **Activate the pre-created virtual environment:**

    Windows (PowerShell):
    PowerShell

    .\venv\Scripts\Activate.ps1

    Linux/macOS:
    Bash

    source venv/bin/activate
3. **Install dependencies:**
    Bash

    pip install -r requirements.txt

## Running the Webhook Receiver

    Start the Flask server:
    Bash

    python app.py

    The app will run locally on http://127.0.0.1:5000.
## Send a test payload:
Open a separate terminal window and run:

    PowerShell:
    PowerShell

    Invoke-RestMethod -Uri [http://127.0.0.1:5000/webhook](http://127.0.0.1:5000/webhook) -Method Post -ContentType "application/json" -Body '{"event": "payment_success", "user_id": 102, "amount": 49.99}'

    cURL (Linux/macOS/CMD):
    Bash

    curl -X POST [http://127.0.0.1:5000/webhook](http://127.0.0.1:5000/webhook) -H "Content-Type: application/json" -d "{\"event\": \"payment_success\", \"user_id\": 102, \"amount\": 49.99}"

## Check the logs:
Received payloads will automatically append to webhook_logs.json in the root directory.

## Project Structure
Plaintext

├── app.py               # Main Flask application and webhook route
├── JOURNAL.md           # Learning journal & blocker logs
├── requirements.txt     # Python package dependencies
├── webhook_logs.json    # Local storage for received payloads
└── .gitignore           # Git ignore rules
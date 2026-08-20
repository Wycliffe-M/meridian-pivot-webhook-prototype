# Learning & Blocker Journal — Assignment 1 (Webhooks)

**Learner:** Wycliffe-M
**Unfamiliar tool:** Webhooks
**Time-box:** Day 1–2

---

## 1. Time Log

| Date | Time started | Time ended | Total time spent |
|------|--------------|------------|------------------|
| 2026-08-20 | 20:00 -| 21:20 -----|   1 hr 20 mins   |

---

## 2. Resources Consulted

| # | Resource (title/link) | What you were trying to figure out | What you took away from it |
|---|---|---|---|
| 1 | Flask Official Documentation | How to route POST requests and parse incoming JSON | `@app.route` with `methods=["POST"]` handles incoming webhooks, and `request.get_json()` parses the incoming data payload. |
| 2 | Microsoft PowerShell Documentation | Fixing header/cURL parameter binding errors in PowerShell | PowerShell maps `curl` to `Invoke-WebRequest` by default; using `Invoke-RestMethod` is the native way to send JSON payloads. |

---

## 3. Blocker Log

### Blocker 1
- **What I was trying to do:** Run the Flask application using `python app.py`.
- **What went wrong (error message, unexpected behavior, confusion):** Got `SyntaxError: invalid syntax` pointing to line 28 of `app.py`.
- **What I tried first:** Executing `python app.py` in the terminal.
- **Why that didn't work:** I accidentally pasted the command string `python app.py` inside the actual Python file rather than executing it in the terminal CLI.
- **What actually resolved it:** Removed `python app.py` from the code file, saved it, and executed the command directly inside the VS Code terminal.
- **Time spent stuck:** ~5 mins

### Blocker 2
- **What I was trying to do:** Send a POST request to test the `/webhook` endpoint using `curl` in PowerShell.
- **What went wrong (error message, unexpected behavior, confusion):** Received `ParameterBindingException: Cannot bind parameter 'Headers'` because PowerShell maps `curl` to `Invoke-WebRequest`.
- **What I tried first:** Running a standard Bash-style `curl` command.
- **Why that didn't work:** PowerShell's alias interprets `-H` differently than standard cURL syntax.
- **What actually resolved it:** Used `Invoke-RestMethod` with native PowerShell parameters (`-Uri`, `-Method`, `-ContentType`, `-Body`).
- **Time spent stuck:** ~10 mins

---

## 4. What I Understand Now (End of Day 2)

- **Webhook vs. Polling:** Polling requires a client to repeatedly request data from a server at fixed intervals to check for updates. A webhook reverses this by having the server automatically push an HTTP POST request to a client endpoint only when an event occurs.
- **Environment Setup:** Virtual environment (`venv`) setup and package activation were initialized prior to dependencies installation and server implementation.
- **Receiving Webhooks:** An endpoint route listens for incoming HTTP requests, validates the payload header/JSON body, processes or logs the data, and returns an immediate HTTP status response (e.g., `200 OK`) to acknowledge receipt.
- **Future Considerations:** To use webhooks in production, I would need to implement payload signature verification (HMAC secret keys) for security, use a public tunneling service (like ngrok) or host the server online, and add proper queueing or database storage.


---

## 5. Mini-Prototype Summary

- **What it does:** Runs a local Flask server that exposes a `/webhook` POST endpoint, intercepts JSON payloads, appends server timestamps, and logs them locally to `webhook_logs.json`.
- **How to run it:**
  1. Activate virtual environment: `.\venv\Scripts\Activate.ps1`
  2. Start server: `python app.py`
  3. Send test webhook in a separate terminal:
     `Invoke-RestMethod -Uri http://127.0.0.1:5000/webhook -Method Post -ContentType "application/json" -Body '{"event": "payment_success", "user_id": 102, "amount": 49.99}'`
- **What it does NOT do / known limitations:** Does not authenticate requests, run on a public URL, or use a persistent database.
- **Link/path to code:** `app.py`

---

## 6. Honest Self-Note

Starting out, the concept of a webhook sounded complex, but building a receiver made me realize it is just a standard HTTP POST request triggered by an event. Dealing with PowerShell-specific aliases was slightly frustrating at first, but working through the terminal errors gave me a clearer understanding of client-server interactions.
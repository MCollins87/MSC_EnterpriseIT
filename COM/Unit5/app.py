# app.py
import os
import logging
from flask import Flask, jsonify

app = Flask(__name__)

# 12-Factor: config from environment
ENV = os.getenv("ENV", "development")
PORT = int(os.getenv("PORT", 8080))
GREETING = os.getenv("GREETING", "Hello from Mark's 12-Factor app!")

# 12-Factor: logs to stdout
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

@app.route("/")
def index():
    logger.info("Handling request to /")
    return jsonify({"env": ENV, "message": GREETING})

@app.route("/healthz")
def health():
    return "ok", 200

if __name__ == "__main__":
    # For local dev only; production use gunicorn (below)
    app.run(host="0.0.0.0", port=PORT)

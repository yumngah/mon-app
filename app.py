from flask import Flask
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)
REQUESTS = Counter("app_requests_total", "Nombre de requetes")

@app.route("/")
def home():
    REQUESTS.inc()
    return "Bonjour depuis Docker - version 1"

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

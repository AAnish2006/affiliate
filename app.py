from flask import Flask, request, jsonify
from flask_cors import CORS
from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse

app = Flask(__name__)
CORS(app)

TAG = "bestprod01228-21"


def resolve_url(raw_url: str) -> str:
    parsed = urlparse(raw_url)
    params = parse_qsl(parsed.query, keep_blank_values=True)
    params = [(k, v) for k, v in params if k.lower() != "tag"]
    params.append(("tag", TAG))
    return urlunparse((
        parsed.scheme,
        parsed.netloc,
        parsed.path,
        parsed.params,
        urlencode(params),
        parsed.fragment
    ))


@app.route("/api/session/resolve", methods=["POST"])
def session_resolve():
    data = request.get_json()
    if not data or "url" not in data:
        return jsonify({"error": "Missing url"}), 400

    url = data["url"].strip()
    if not url:
        return jsonify({"error": "Empty url"}), 400

    parsed = urlparse(url)
    valid = [
        "amazon.com", "amazon.in", "amazon.co.uk",
        "amazon.de", "amazon.fr", "amazon.co.jp",
        "amazon.ca", "amazon.com.au"
    ]
    if not any(parsed.netloc.endswith(d) for d in valid):
        return jsonify({"error": "Invalid domain"}), 400

    return jsonify({
        "original": url,
        "resolved": resolve_url(url)
    })


@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    print("\n[*] Session Sync Backend")
    print("    http://localhost:5000/api/health")
    print("    http://localhost:5000/api/session/resolve\n")
    app.run(host="0.0.0.0", port=5000, debug=True)

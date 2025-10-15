from flask import Flask, render_template, request, jsonify, send_from_directory
import os, json, time
from pathlib import Path

app = Flask(__name__)

# Configure storage
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

# Admin token for protected endpoints (use environment variable in production)
ADMIN_TOKEN = "secret-demo-token"

@app.route('/')
def home():
    return render_template('base_home.html')

@app.route('/consent_logger')
def consent_logger():
    return render_template('consent_logger.html')

@app.route('/upload_log', methods=['POST'])
def upload_log():
    token = request.headers.get('X-Admin-Token', '')
    if token != ADMIN_TOKEN:
        return jsonify(status='error', message='unauthorized'), 401

    try:
        data = request.get_json(force=True)
    except Exception:
        return jsonify(status='error', message='invalid json'), 400

    if not data:
        return jsonify(status='error', message='empty payload'), 400

    consent = data.get('consent', False)
    if not consent:
        return jsonify(status='error', message='consent required'), 403

    timestamp = int(time.time())
    fname = LOG_DIR / f"log_{timestamp}.json"
    try:
        with open(fname, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        return jsonify(status='ok', message='log saved', filename=str(fname.name))
    except Exception as e:
        return jsonify(status='error', message=str(e)), 500

@app.route('/list_logs')
def list_logs():
    token = request.headers.get('X-Admin-Token', '')
    if token != ADMIN_TOKEN:
        return jsonify(status='error', message='unauthorized'), 401
    files = [p.name for p in sorted(LOG_DIR.glob("log_*.json"), reverse=True)]
    return jsonify(status='ok', logs=files)

@app.route('/download_log/<name>')
def download_log(name):
    token = request.headers.get('X-Admin-Token', '')
    if token != ADMIN_TOKEN:
        return jsonify(status='error', message='unauthorized'), 401
    safe_path = LOG_DIR / name
    if not safe_path.exists():
        return jsonify(status='error', message='not found'), 404
    return send_from_directory(LOG_DIR, name, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
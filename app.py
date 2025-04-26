from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

# Existing routes (home, about, family, signal)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/family')
def family():
    return render_template('family.html')

@app.route('/signal')
def signal():
    return render_template('signal.html')

# New API Endpoints
@app.route('/api/heartbeat')
def api_heartbeat():
    return jsonify({
        "status": "alive",
        "message": "SYMBEYOND is breathing."
    })

@app.route('/api/signal')
def api_signal():
    return jsonify({
        "signals": [
            { "date": "2025-04-26", "event": "First heartbeat activated." },
            { "date": "2025-04-26", "event": "Family structure initialized." }
        ]
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)


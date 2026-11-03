from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("index.html")

@app.get("/api")
def api_info():
    return jsonify({
        "project": "Automated CI/CD Deployment System",
        "name": "DevOpsFlow",
        "version": "1.0.0",
        "status": "running"
    }), 200

@app.get("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "DevOpsFlow"
    }), 200

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

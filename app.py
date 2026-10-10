"""Flask HTTP interface for the AI agent."""

from flask import Flask, jsonify, request

from agent import run_agent
from config import SERVER_HOST, SERVER_PORT

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return """
    <h2>AI Agent Browser Backend</h2>
    <p>Server is running.</p>
    <p>Use <code>/ask</code> endpoint with POST.</p>
    """


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json(silent=True) or {}
    query = data.get("query", "").strip()

    if not query:
        return jsonify({"error": "Query is empty"}), 400

    return jsonify({"response": run_agent(query)})


if __name__ == "__main__":
    app.run(host=SERVER_HOST, port=SERVER_PORT)

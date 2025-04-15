# backend/app.py
from flask import Flask, jsonify

# Initialize Flask app
app = Flask(__name__)

# Define a test route
@app.route('/api/test', methods=['GET'])
def test():
    return jsonify({
        "message": "Nexora is online! Vexora's tampering detected: 0 ✅"
    })

# Run the server
if __name__ == '__main__':
    app.run(debug=True)
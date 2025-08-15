from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Calculator API!"})

@app.route('/add', methods=['GET'])
def add():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    return jsonify({"operation": "addition", "a": a, "b": b, "result": a + b})

@app.route('/subtract', methods=['GET'])
def subtract():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    return jsonify({"operation": "subtraction", "a": a, "b": b, "result": a - b})

@app.route('/multiply', methods=['GET'])
def multiply():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    return jsonify({"operation": "multiplication", "a": a, "b": b, "result": a * b})

@app.route('/divide', methods=['GET'])
def divide():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 1))
    if b == 0:
        return jsonify({"error": "Division by zero not allowed"}), 400
    return jsonify({"operation": "division", "a": a, "b": b, "result": a / b})

if __name__ == '__main__':
    app.run(debug=True)


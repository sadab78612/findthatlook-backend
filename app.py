from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to FindThatLook Backend API!"})

@app.route('/api/hello')
def hello():
    return jsonify({"message": "Hello Sadab! Your app is running successfully."})

if __name__ == '__main__':
    app.run(debug=True)
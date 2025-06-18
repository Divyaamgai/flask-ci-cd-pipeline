from flask import Flask

app = Flask(__name__)

@app.route('/hello')  # Corrected the curly quote to a straight quote
def hello():
    return "Hello, DevOps!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

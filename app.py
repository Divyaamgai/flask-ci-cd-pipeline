from flask import Flask
from flask_talisman import Talisman

app = Flask(__name__)
Talisman(app)

@app.route('/hello') 
def hello():
    return "Hello, DevOps!"


@app.route('/hi') 
def hi():
    return "Hi!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000 debug=False)

#hi

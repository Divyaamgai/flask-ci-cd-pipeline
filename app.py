from flask import Flask
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

# Define a counter for each route
hello_counter = Counter('hello_requests_total', 'Total /hello requests')
hi_counter = Counter('hi_requests_total', 'Total /hi requests')
yes_counter = Counter('yes_requests_total', 'Total /yes requests')

@app.route('/hello')
def hello():
    hello_counter.inc()
    return "Hello, DevOps! this is in class"

@app.route('/hi')
def hi():
    hi_counter.inc()
    return "Hi!"

@app.route('/yes')
def yes():
    yes_counter.inc()
    return "Yes!"

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain; version=0.0.4; charset=utf-8'}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)

#hi

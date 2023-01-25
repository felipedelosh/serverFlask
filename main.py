from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World"

@app.route('/health')
def health():
    return "Server is OK"

#Start
if __name__ == '__main__':
    app.run(host='0.0.0.0' ,debug=True, port=4000)
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "User Management Service"

@app.route('/test')
def test():
    return "Test"

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/test")
def test():
    return "<h1>Test!</h1>"


if __name__ == "__main__":
    app.run(debug=True)

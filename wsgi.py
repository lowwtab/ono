from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello World!</h1>"

if __name__ == "main":
    app.ru(host="0.0.0.0")

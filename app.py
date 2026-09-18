from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return ("hy nashath")

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, redirectq, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", content="testing")


if __name__ == "__main__":
    app.run()
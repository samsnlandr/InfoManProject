from flask import Flask, redirect, url_for, render_template, request
#TODO /Submit Route form.gets
app = Flask(__name__)

@app.route("/")
def home():
    return redirect(url_for("fill_out_forms"))

@app.route("/Card_Holder_Application_Form")
def fill_out_forms():
    return render_template("index.html")

@app.route("/submit")
def submit():
    if request.method == "POST":
        values = request.form.get("")
        return redirect(url_for("work_forms"))

@app.route("/About_Work_Form")
def work_forms():
    return render_template("about_work.html")

if __name__ == "__main__":
    app.run(debug = True)
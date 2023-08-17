from flask import Flask, render_template
app = Flask("hegemony-website")

@app.route("/")
def start():
    return render_template("index.html")
app.run(debug = True)
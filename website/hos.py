from flask import Flask, render_template

hos = Flask(__name__)

@hos.route("/")
def index():
    return render_template("index.html")

@hos.route("/about")
def about():
    return render_template("about.html")

@hos.route("/data")
def data():
    return render_template("data.html")

if __name__=="__main__":
    hos.run(debug=True)
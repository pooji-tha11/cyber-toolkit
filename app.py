from flask import Flask, render_template, request
from modules.password_analyser import analyze_password


app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template("index.html")


@app.route("/password", methods = ["GET", "POST"])
def password_page():
    result = None
    if request.method == "POST":
        password = request.form.get("password", "")
        result = analyze_password(password)
    return render_template("password.html", result = result)

if __name__ == '__main__':
    app.run(debug=True)


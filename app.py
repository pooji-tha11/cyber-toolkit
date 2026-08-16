from flask import Flask, render_template, request
from modules.password_analyser import analyze_password
from modules.hash_generator import generate_hashes, generate_file_hashes
from modules.url_analyzer import analyze_url

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

@app.route("/hash", methods = ["GET", "POST"])
def hash_page():
    result = None
    input_text = ""
    filename = None

    if request.method == "POST":
        uploaded_file = request.files.get("file")

        if uploaded_file and uploaded_file.filename:
            filename = uploaded_file.filename
            file_bytes = uploaded_file.read()
            result = generate_file_hashes(file_bytes)
        else:
            input_text = request.form.get("text", "")
            if input_text:
                result = generate_hashes(input_text)

    return render_template("hash.html", result=result, input_text=input_text, filename=filename)

@app.route("/url", methods=["GET", "POST"])
def url_page():
    result = None
    input_url = ""
    if request.method == "POST":
        input_url = request.form.get("url", "")
        result = analyze_url(input_url)
    return render_template("url.html", result=result, input_url=input_url)

if __name__ == '__main__':
    app.run(debug=True)


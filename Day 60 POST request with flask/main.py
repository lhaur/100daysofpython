from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def receive_data():
    name = request.form['name']
    password = request.form['password']
    print(request.form)
    return f"Name: {name}, password: {password}"

if __name__ == "__main__":
    app.run(debug=True)
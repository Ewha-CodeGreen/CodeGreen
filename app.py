from flask import Flask, render_template

app = Flask(__name__)

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/home")
def view_home():
    return render_template("home.html")

@app.route("/mypage")
def view_review():
    return render_template("mypage.html")

@app.route("/productList")
def reg_item():
    return render_template("productList.html")

if __name__ == "__main__":
    app.run(debug=True)

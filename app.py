from flask import Flask, render_template

app = Flask(__name__)

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/productDetail")
def view_produceDetail():
    # 예시로 product 정보를 설정했습니다.
    product = {
        'seller_nickname': '이화인',
        'category': '생활 용품',
        'name': '물병',
        'price': 15000,
        'location': '서울특별시',
        'status': '새상품',
        'rating': 4.5,
        'stock': 10,
        'description': '이 물병은 매우 튼튼하고 가벼워요!',
        'reviews': ['좋아요!', '배송 빠르고 상품 좋아요.', '생각보다 크네요.']
    }
    return render_template("productDetail.html", product=product)

@app.route("/mypage")
def view_review():
    return render_template("mypage.html")

@app.route("/productList")
def reg_item():
    return render_template("productList.html")

if __name__ == "__main__":
    app.run(debug=True)
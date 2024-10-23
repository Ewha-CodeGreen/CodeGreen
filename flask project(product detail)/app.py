from flask import Flask, render_template

app = Flask(__name__)

# 예시 데이터: 상품 정보
products = {
    1: {
        "name": "상품 A",
        "description": "상품 A의 상세 설명",
        "price": 10000,
        "seller_nickname": "판매자A",
        "category": "초록템",
        "location": "서울",
        "status": "새상품",
        "stock": 10,
        "reviews": ["좋아요", "만족합니다"],
        "rating": 4.5,
    },
}

@app.route("/")
def home():
    return "홈페이지입니다."

@app.route("/products")
def products_list():
    return "상품 목록 페이지입니다."

@app.route("/about")
def about():
    return "소개 페이지입니다."

@app.route("/product/<int:product_id>")
def product_detail(product_id):
    product = products.get(product_id)
    if product:
        return render_template("productdetail.html", product=product)
    else:
        return "상품을 찾을 수 없습니다.", 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

from flask import Flask, render_template

application = Flask(__name__)

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

@application.route("/")
def index():
    return render_template("index.html", products=products)

if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=True)

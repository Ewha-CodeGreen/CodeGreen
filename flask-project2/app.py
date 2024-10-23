from flask import Flask, render_template, request, redirect, url_for
import os

application = Flask(__name__)

# 업로드할 파일의 저장 경로 설정
UPLOAD_FOLDER = 'uploads'
application.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 업로드 폴더 생성
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

products = {}

@application.route("/", methods=["GET", "POST"])
def reg_item():
    if request.method == "POST":
        name = request.form.get("name")
        seller = request.form.get("seller")
        addr = request.form.get("addr")
        category = request.form.get("category")
        status = request.form.get("status")
        price = request.form.get("price", type=float)
        stock = request.form.get("stock", type=int)

        # 이미지 파일 처리
        image = request.files['image']
        image_filename = f"{len(products) + 1}_{image.filename}"
        image.save(os.path.join(application.config['UPLOAD_FOLDER'], image_filename))

        product_id = len(products) + 1
        products[product_id] = {
            "name": name,
            "description": "상품 설명을 여기에 입력하세요",
            "price": price,
            "seller_nickname": seller,
            "category": category,
            "location": addr,
            "status": status,
            "stock": stock,
            "image": image_filename,  # 이미지 파일 이름 저장
            "reviews": [],
            "rating": 0,
        }

        return redirect(url_for("product_detail", product_id=product_id))

    return render_template("register.html")

@application.route("/product/<int:product_id>")
def product_detail(product_id):
    product = products.get(product_id)
    if product:
        return render_template("product_detail.html", product=product)
    return "상품을 찾을 수 없습니다.", 404

if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=True)

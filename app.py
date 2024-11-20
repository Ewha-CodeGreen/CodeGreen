import logging
from flask import Flask, render_template, request, redirect, url_for, session
from database import DBhandler
import os

app = Flask(__name__)
app.secret_key = 'super_secret_key'
DB = DBhandler()

# 디버깅 로그 설정
logging.basicConfig(level=logging.DEBUG)

# 업로드 폴더 설정
UPLOAD_FOLDER = os.path.join('static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# 기본 세션 값 설정
@app.before_request
def set_default_session_values():
    if 'role' not in session:
        session['role'] = 'buyer'

# 홈 페이지
@app.route("/")
def home():
    return render_template("homeBuyer.html", logged_in=('id' in session), user=session.get('nickname'))

# 상품 리스트
@app.route("/browse", methods=["GET"])
def browse():
    try:
        # Firebase에서 데이터 가져오기
        all_products = DB.get_items()  # 리스트로 반환된 데이터
        logging.debug(f"DEBUG: All Products from Firebase: {all_products}")

        # 리스트 형식 확인 및 유효 데이터 필터링
        if isinstance(all_products, list):
            valid_products = [product for product in all_products if product is not None]
        else:
            # 예외 처리: 리스트가 아닌 경우 빈 리스트로 설정
            valid_products = []

        # 페이지네이션 처리
        page = request.args.get('page', default=1, type=int)
        items_per_page = 4
        total_products = len(valid_products)
        total_pages = (total_products + items_per_page - 1) // items_per_page

        if page < 1:
            page = 1
        elif page > total_pages:
            page = total_pages

        start_idx = (page - 1) * items_per_page
        end_idx = start_idx + items_per_page
        products = valid_products[start_idx:end_idx]

        # 각 제품에 대한 기본 필드 설정
        for product in products:
            product["img_path"] = product.get("img_path", "default.jpg")

        return render_template(
            "browseBuyer.html",
            products=products,
            page=page,
            total_pages=total_pages
        )
    except Exception as e:
        logging.error(f"Error loading products: {e}")
        return f"Error loading products: {str(e)}", 500

# 상품 상세 페이지
@app.route("/view_detail/<product_name>/")
def product_detail(product_name):
    try:
        logging.debug(f"Requested product name: {product_name}")
        all_products = DB.get_items()  # 리스트 반환
        logging.debug(f"All products: {all_products}")

        # 리스트에서 이름으로 상품 검색
        product = next((item for item in all_products if item and item.get("name") == product_name), None)

        if not product:
            logging.error(f"Product with name '{product_name}' not found.")
            return f"Product '{product_name}' not found", 404

        return render_template(
            "productDetailBuyer.html",
            product=product,
            logged_in=('id' in session),
            user=session.get('nickname')
        )
    except Exception as e:
        logging.error(f"Error retrieving product details: {e}")
        return f"An unexpected error occurred: {str(e)}", 500



# 상품 등록
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # 상품 등록 데이터 수집
        name = request.form.get("name")
        price = float(request.form.get("price").replace('₩', '').replace(',', ''))
        category = request.form.get("category")
        description_short = request.form.get("description_short")
        description_long = request.form.get("description_long")

        # 이미지 처리
        image = request.files['file']
        image_filename = f"{name}_{image.filename}"
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_filename)
        image.save(image_path)

        # Firebase에 저장할 데이터 구성
        product_data = {
            "name": name,
            "price": price,
            "category": category,
            "description_short": description_short,
            "description_long": description_long,
            "img_path": image_filename
        }

        # Firebase에 데이터 저장
        product_id = str(len(DB.get_items()) + 1)
        if DB.insert_item(product_id, product_data):
            return redirect(url_for("browse"))
        return render_template("error.html", message="상품 등록에 실패했습니다.")

    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)

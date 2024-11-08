from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = 'super_secret_key'  # 세션 관리를 위한 키 설정

# 업로드할 파일의 저장 경로 설정
UPLOAD_FOLDER = os.path.join('static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 업로드 폴더 생성
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# 가상 데이터베이스 예시 데이터
products = {
    1: {
        "seller_nickname": "seller_nickname",
        "label": "ewhagreen",
        "image_url": "path_to_image/gel_pen.jpg",
        "name": "이화그린 펜 (5set)",
        "price": 6500,
        "status": "새상품입니다.",
        "description": "This is a new set of pens.",
        "rating": 5
    },
    2: {
        "seller_nickname": "seller_nickname",
        "label": "ewhagreen",
        "image_url": "path_to_image/bear_keychain.jpg",
        "name": "이화 곰돌이 키링",
        "price": 5000,
        "status": "gently used, perfect for collectors",
        "description": "A collectible bear keychain.",
        "rating": 5
    },
    3: {
        "seller_nickname": "seller_nickname",
        "label": "ewhagreen",
        "image_url": "path_to_image/bunny_keychain.jpg",
        "name": "이화 버니 키링",
        "price": 5500,
        "status": "새상품입니다.",
        "description": "A cute bunny keychain.",
        "rating": 5
    },
    4: {
        "seller_nickname": "seller_nickname",
        "label": "ewhagreen",
        "image_url": "path_to_image/bag.jpg",
        "name": "이화 가방",
        "price": 15000,
        "status": "새상품입니다.",
        "description": "A spacious and stylish bag.",
        "rating": 5
    }
}

users = {
    "testuser@example.com": {
        "user_id": "testuser",
        "password": "password",
        "nickname": "test_nickname"
    }
}

@app.route("/index")
def index():
    return render_template("index.html", logged_in=('user_id' in session), user=session.get('nickname'))

@app.route("/")
def home():
    return render_template("homeBuyer.html", logged_in=('user_id' in session), user=session.get('nickname'))

@app.route("/signUp", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        user_id = request.form.get("user-id")
        password = request.form.get("password")
        nickname = request.form.get("nickname")
        email = request.form.get("email")

        # 사용자 정보를 딕셔너리에 저장
        users[email] = {
            "user_id": user_id,
            "password": password,
            "nickname": nickname
        }

        # 회원가입 후 세션에 저장하여 자동 로그인 처리
        session['user_id'] = user_id
        session['nickname'] = nickname

        return redirect(url_for("home"))

    return render_template('signUp.html', logged_in=False)

@app.route("/mypage")
def view_review():
    return render_template("mypageBuy.html")


@app.route("/browse")
def browse():
    # Browse 페이지에서 모든 상품 목록을 표시합니다.
    return render_template("browse.html", products=products.values())

@app.route("/register", methods=["GET", "POST"])
def register_item():
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
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], image_filename))

        # 상품 딕셔너리에 추가
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

        return render_template("register.html", success=True)

    return render_template("register.html")

@app.route("/product/<int:product_id>")
def product_detail(product_id):
    product = products.get(product_id)
    if product:
        return render_template("product_detail.html", product=product)
    return "Product not found", 404

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_id = request.form.get("user-id")
        password = request.form.get("password")

        # 로그인 유효성 검사
        for user in users.values():
            if user["user_id"] == user_id and user["password"] == password:
                session['user_id'] = user_id
                session['nickname'] = user['nickname']
                return redirect(url_for("home"))

        return render_template("login.html", error="아이디 또는 비밀번호가 잘못되었습니다.", logged_in=False)
    return render_template("login.html", logged_in=False)

@app.route("/findId", methods=["GET", "POST"])
def find_id():
    if request.method == "POST":
        email = request.form.get("email")

        # 이메일로 아이디 찾기
        if email in users:
            user_id = users[email]["user_id"]
            return render_template("findId.html", user_id=user_id, found=True, logged_in=False)
        else:
            return render_template("findId.html", error="해당 이메일로 가입된 아이디가 없습니다.", logged_in=False)

    return render_template("findId.html", logged_in=False)

@app.route("/logout")
def logout():
    session.pop('user_id', None)
    session.pop('nickname', None)
    return redirect(url_for("home"))

@app.route('/review')
def reviews():
    reviews_data = [
        {"title": "리뷰 제목", "author": "작성자 닉네임", "date": "작성 날짜"},
        {"title": "리뷰 제목", "author": "작성자 닉네임", "date": "작성 날짜"},
        {"title": "리뷰 제목", "author": "작성자 닉네임", "date": "작성 날짜"},
    ]
    return render_template('productreviews.html', reviews=reviews_data)

if __name__ == "__main__":
    app.run(debug=True)

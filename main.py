import datetime

from flask import Flask, request, url_for

app = Flask(__name__)


@app.route('/')
def index():
    user_url = url_for('show_user_profile', username="johndoe")
    post_url = url_for('show_post', year='2024', month='11',day='19')
    return f'User URL : {user_url}<br>Post URL : {post_url}'


@app.route('/post/<year>/<month>/<day>')
def show_post(year,month,day):
    # utc_0 = datetime.datetime.utcnow()
    # korea_time = utc_0 + datetime.timedelta(hours=9)
    # year = korea_time.year
    # month = korea_time.month
    # day = korea_time.day
    return f'Post for {year}/{month}/{day}'

# def show_user_profile(username):
#     return f"User {username}"


@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {username}님의 프로필 페이지입니다. 홈으로 가기: {url_for("index")}'


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return "Logging in ... "
    else:
        return "Login Form"


@app.route('/static-example')
def static_example():
    return f'정적파일 URL : {url_for("static", filename="style.css")}'


# URL 테스트
@app.route('/absolute')
def absolute():
    return f'외부 절대 URL : {url_for("index", _external=True)}'


# HTTPS와 절대 URL TEST
@app.get('/https')
def https():
    return f'HTTPS 절대 URL : {url_for("index", _scheme="https", _external=True)}'
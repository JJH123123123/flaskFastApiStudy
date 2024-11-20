import datetime

from flask import Flask, request, url_for, jsonify, make_response

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


@app.route('/add/<int:num1>/<int:num2>')
def add(num1:int, num2:int):
    return f'test'


@app.route('/int/<int:var>')
def int_type(var: int):
    return f'Integer: {var}'


@app.route('/float/<float:var>')
def float_type(var: float):
    return f'Float: {var}'


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath: {subpath}'


@app.route('/uuid/<uuid:some_id>')
def show_uuid(some_id):
    return f'UUID: {some_id}'



# 요청과 응답

@app.route('/query')
def query_example():
    langauage = request.args.get('language')
    return f"Requested language : {langauage}"


@app.route('/items', strict_slashes=False)
def find_page():
    page = request.args.get('page', default='1')
    sort = request.args.get('sort', default='desc')

    # Validate sort parameter
    if sort not in ['asc', 'desc']:
        return f"Invalid sort value: {sort}", 400
    # Rest of your code
    return f"Requested page: {page} and sort order: {sort}"


# serialize


@app.route('/json', methods=['GET', 'POST'])
def json_example():
    # jsonify
    if request.method == 'POST':
        data = request.json
        print(data)

        return jsonify(data)

    return jsonify({'Hello': ' World!'})
    # jsonify - >  return current_app.json.response(*args, **kwargs)  # type: ignore[return-value]
    # -> return self._app.response_class(self.dumps(obj), mimetype="application/json")




@app.route('/response')
def response_example():
    # 응답 객체 생성

    resp = make_response("Hello with header", 200)

    resp.headers['Custom-Header'] = 'custom-value'

    return resp
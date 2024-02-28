from flask import Flask, request, Response
import test

app = Flask(__name__)

@app.route('/')
def home() :
    return 'Hello, This is Main Page!'

@app.route('/about')
def about() :
    return 'This is the about Page!'

@app.route('/company')
def company() :
    return 'This is the company Page!'

@app.route('/user/<username>')
def user_profile(username) :
    return f'UserName : {username}'

@app.route('/number/<int:number>')
def user_number(number) :
    return f'Number : {number}'

# post 요청 날리는 법
# 1) post man (프로그램) 사용
# 2)  requests 모델 활용
import requests
@app.route('/test')
def test():
    url = "http://127.0.0.1:5000/submit"
    data = 'test data'
    response = requests.post(url=url, data = data)
    return response

@app.route('/submit', methods=['GET', 'POST', 'PUT', 'DELETE'])
def submit() :
    print(request.method)
    # return ' '
    if request.method == 'GET' :
        print("GET method")

    if request.method == 'POST' :
        print("***POST method***", request.data)
    
    return Response("Successfully submitted", status=200)


if __name__ == '__main__':
    app.run()
import os
import sys

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world() -> str:  # put application's code here
    return "Hello World!"


if __name__ == "__main__":
    app.run()

# 정적 vs 동적
# 정적 : 실행 하지 않고 타입 결정
# 동적 : 실행 중 변경, 실행 중 바뀌는 경우
# → mypy : 정적으로 타입 체크 가능. (Edge case에서 유용하게 사용.)

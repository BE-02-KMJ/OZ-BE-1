from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# 라우팅
# 채팅 기능을 실험해보기 위한 html
@app.route('/')
def index():
    return render_template('index.html')

def msg_received(methods=['GET', 'POST']):
    print("CALLBACK : msg_received")
    # DB connection → save

# 소켓 연결 (클라이언트 - 서버)
@socketio.on('my event')
def handle_chat_event(json, methods=['GET', 'POST']):
    print(f'데이터 수신 완료: {json}')

    socketio.emit('my response', json, callback=msg_received)

if __name__ == '__main__':
    socketio.run(app, debug=True)
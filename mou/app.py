from stat import FILE_ATTRIBUTE_NOT_CONTENT_INDEXED
from flask import Flask,render_template,request
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)

socketio = SocketIO(app)

user_count = 0
text = ""

@app.route('/')
def index():
    return render_template('./index.html')



if __name__ == '__main__':
    socketio.run(app, debug=True)
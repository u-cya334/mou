from flask import Flask,request
from flask import render_template
from flask_socketio import SocketIO, send, emit, join_room

app = Flask(__name__)
socketio= SocketIO(app)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/room/<room_id>')
def room(room_id):
    return render_template('room.html',room_id)

@app.route('/test/<number>')
def test(number):
    return render_template('test.html',number)

@socketio.on("my event")
def socket_test(table_id):
    print(table_id)
    emit("new_game",room=table_id, broadcast=True)

@socketio.on("join")
def join(table_id):
    print(table_id)
    join_room(table_id)


if __name__ == "__main__":
    socketio.run(app,debug=True)
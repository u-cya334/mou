from xml.etree.ElementInclude import include
from flask import Flask,request
from flask import render_template
from flask_socketio import SocketIO, send, emit, join_room
import random

app = Flask(__name__)
socketio= SocketIO(app)
card_list = []

# カードの中身を決める
def card_shafle():
    global card_list
    card_list = [0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14]
    card_list = random.sample(card_list,len(card_list))
    print(card_list)

@app.route('/')
def home():
    global card_list
    card_shafle()
    return render_template('test.html',card_list=card_list)

@app.route('/room/<room_id>')
def room(room_id):
    return render_template('room.html',room_id)

@app.route('/test/<number>')
def test(number):
    return render_template('test.html',number)

@socketio.on("start_newgame")
def socket_test():

    emit("newgame",broadcast=True,include_self = False)

@socketio.on("join")
def join(table_id):
    print("python table_id:"+str(table_id))
    join_room(table_id)
    
user_count = 0
text = ""


@socketio.on("connect")
def connect():
    global user_count,text
    print("接続！！")
    user_count += 1
    # emit jsファイルの関数呼び出し
    emit("counter",{"user_count":user_count},broadcast=True)
    emit("text_update",{"text":text})

@socketio.on("disconnect")
def disconnect():
    global user_count
    user_count -= 1
    emit("counter",{"user_count":user_count},broadcast=True)

@socketio.on("text_update")
def text_update(json):
    global text
    text = json["text"]
    emit("text_change",{"text":text},broadcast=True, include_self=False)
    
@socketio.on('share_card')
def share_card(num):
    emit("show_card",{"num":num["num"]},broadcast=True, include_self=False)



if __name__ == "__main__":
    socketio.run(app,debug=True)
const socket = io();


// 識別用のIDを作成
let id_number = Math.floor(Math.random() * 1000000)
console.log(id_number)

// つながったときの処理
socket.on('connect',function(){
    console.log("hi")
})

const join = function(){
    console.log("joinしました")
    socket.emit('join',334)
}

// ゲームスタート
const newgame1 = function(){
    console.log("newgame!!")

    
}

// ゲームが始まると他の人の分もはじめる
socket.on("newgame",function(){
    console.log(test._data.start_show)
    test._data.start_show = true
})

// 現在の接続人数
socket.on("counter",function(msg){
    console.log(document.getElementById("counter").textContent)
    document.getElementById("counter").textContent = msg.user_count
})



// 他の人がめくったカードを反映させる
socket.on("show_card",function(num){
    console.log(num.num)
    document.getElementById(num.num).setAttribute('src',`/static/img/${num.num}.png`)
})

socket.on("")

let card1 = document.getElementById("0")

const test = new Vue({
    el:"#app",
    data:{
        test_name: "testdesu",
        list: 32,
        start_show:false
    },
    methods:{
        button1:function (event) { 
            join()
        },
        start:function(){
            console.log(this.start_show)
            this.start_show = true;
            socket.emit("start_newgame")
        },
        pick_up:function(num){
            // カードをクリックしたときの動作
            console.log(num)
            card1 = document.getElementById(num)
            card1.setAttribute('src',`/static/img/${num}.png`);
            console.log(card1.getAttribute('src'))
            socket.emit("share_card",{"num":num})
        }
    },
})


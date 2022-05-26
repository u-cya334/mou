const socket = io();
socket.on('connect',function(){
    socket.emit('my event',{data:"connected"})
})

const join = function(){
    socket.emit('join',334)
}
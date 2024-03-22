var set_time  = document.getElementById('time_display_js')

setInterval(()=>{
    var time = new Date()
    set_time.innerHTML = time.toLocaleTimeString()
},1000)


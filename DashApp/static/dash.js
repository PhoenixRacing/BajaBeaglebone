 
//Opens a socket with the server.
//Updates the speed, previous time, current time,
//throttle percentage and brake percentage. 

var start_time = new Date();

$(document).ready(function(){
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    
    //updates the car speed
    socket.on('updateSpeed', function(msg) {
        $('#speed_list').html('<span>' + msg.speed + '</span>');
    });
    setInterval(getSpeed, 180);
    function getSpeed() {
        socket.emit('update', {data : {}});    
    }

    //updates the time and displays on the testing dashboard
    socket.on('updateTime', function(msg) {
        $('#prev_time').html('<p>' + msg.prev + '</p>');
        $('#curr_time').html('<p>' + msg.curr + '</p>');
    });
    setInterval(getPtime, 100);
    function getPtime() {
        socket.emit('update time', {data : {}});
    }


    //Updates the throttle fill bar (to the right of the speed)
    //Updates the brake fill bar (to the left of the speed)
    socket.on('updateBrake', function(msg) {
        var b_percent = (1 - msg.brake) * 100;
        var str_b_percent = b_percent.toString();
        var brake = str_b_percent.concat("%");
        $(".brake_bar_fill").css( "height", brake);

    });
    setInterval(getBrake, 80);
    function getBrake() {
        socket.emit('update brake', {data : {}});
    }  

    socket.on('updateThrottle', function(msg) {
        var throt_p =  (1 - msg.throttle)*100;
        var str_throttle = throt_p.toString();
        var throttle = str_throttle.concat("%");
        $(".throttle_bar_fill").css("height", throttle);
    });
    setInterval(getThrottle, 80);
    function getThrottle() {
        socket.emit('update throttle', {data : {}});
    }  


    //Display an L if wheel lock, an S if wheel spin
    socket.on('updateSL', function(msg) {
        var spin_flag = msg.spin.toString();
        var lock_flag = msg.lock.toString();

        //Uncomment the following to get spin and lock display
        /*if (spin_flag == "1") {
            var spin = "S";}
        else {
            var spin = "";}

        if (lock_flag == "1") {
            var lock = "L";}
        else {
            var lock = "";}

        $('#spin').html('<strong>' + spin + '</strong>');
        $('#lock').html('<strong>' + lock + '</strong>');*/
    })
    setInterval(getSpinLock, 200);
    function getSpinLock() {
        socket.emit('update spin_lock', {data: {}});
    }  

    //Background color is red if we need to go to the pit
    socket.on('updatePit', function(msg) {
        var pit_flag = msg.pit.toString();

        if (pit_flag == "1") {
            var pit = "#D00000";
        }
        else {
            var pit = "#080808";
        }

        $("body").css("background-color", pit);
    })

    setInterval(getPit, 200);
    function getPit() {
        socket.emit('update pit', {data:{}});
    }

    setInterval(getTime, 200);
    function getTime(){
        var now = new Date();
        var dt = now - start_time;
        $('#total_time').text(hourString(dt) + ':' + minuteString(dt) + ':' + secondString(dt));
    }

 });

function minuteString(time){
    var minutes = Math.floor(time/60000) % 60;
    minutes = minutes.toString();
    if (minutes.length < 2){
        minutes = '0' + minutes;
    }
    return minutes
}
function secondString(time){
    var seconds = ((time/1000) % 60).toFixed(2);
    seconds = seconds.toString()
    if (seconds.length < 4){
        seconds = '0' + seconds;
    }
    return seconds
}
function hourString(time){
    var hours = Math.floor(time/3600000)
    hours = hours.toString();
    return hours
}
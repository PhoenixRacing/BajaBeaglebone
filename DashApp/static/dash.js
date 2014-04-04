 
//Opens a socket with the server.
//Updates the speed, previous time, current time,
//throttle percentage and brake percentage. 

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
    socket.on('updateBrakeThrottle', function(msg) {
        var b_percent = msg.brake * 100;
        var str_b_percent = b_percent.toString();
        var brake = str_b_percent.concat("%");
        $(".brake_bar_fill").css( "height", brake );

        var throt_p =  msg.throttle*100;
        var str_throttle = throt_p.toString();
        var throttle = str_throttle.concat("%");
        $(".throttle_bar_fill").css("height", throttle );
    });
    setInterval(getBrakeThrottle, 80);
    function getBrakeThrottle() {
        socket.emit('update brake_throttle', {data : {}});
    }  


    //Display an L if wheel lock, an S if wheel spin
    socket.on('updateSL', function(msg) {
        $('#spin').html('<strong>' + msg.spin + '</strong>');
        $('#lock').html('<strong>' + msg.lock + '</strong>');
    })
    setInterval(getSpinLock, 200);
    function getSpinLock() {
        socket.emit('update spin_lock', {data: {}});
    }  


 });

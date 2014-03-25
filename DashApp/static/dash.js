 
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

    //updates the previous time and displays on the testing dashboard
    socket.on('updatePtime', function(msg) {
        $('#prev_time').html('<p>' + msg.prev + '</p>');
    });
    setInterval(getPtime, 100);
    function getPtime() {
        socket.emit('update ptime', {data : {}});
    }

    //updates the current time and displays on the testing dashboard
    socket.on('updateCtime', function(msg) {
        $('#curr_time').html('<p>' + msg.curr + '</p>');
    });
    setInterval(getCtime, 100);
    function getCtime() {
        socket.emit('current time', {data : {}});
    }

    //updates the brake fill and displays to the left of the speed
    socket.on('updateBrake', function(msg) {
        var b_percent = msg.brake * 100;
        var str_b_percent = b_percent.toString();
        var brake = str_b_percent.concat("%");
        $(".brake_bar_fill").css( "height", brake );
    });
    setInterval(getBrake, 80);
    function getBrake() {
        socket.emit('update brake', {data : {}});
    }

    //updates the throttle fill and displays to the right of the speed
    socket.on('updateThrottle', function(msg) {
        var throt_p =  msg.throttle*100;
        var str_throttle = throt_p.toString();
        var throttle = str_throttle.concat("%");
        $(".throttle_bar_fill").css("height", throttle );
    });
    setInterval(getThrottle, 80);
    function getThrottle() { 
        socket.emit('update throttle', {data : {}});
    }

    //Displays an S if wheel spinning 
    socket.on('updateSpin', function(msg) {
        var spin = msg.spin;
        if (spin) {
            $(".upper_left").css("color", "#D80000");
        }
    })
    setInterval(getSpin, 200);
    function getSpin() {
        socket.emit('update spin', {data: {}});
    }

    //Display an L if wheel locking
    socket.on('updateLock', function(msg) {
        var lock = msg.lock;
        if (lock) {
            $(".upper_right").css("color", "#D80000");
        }
    })
    setInterval(getLock, 200);
    function getLock() {
        socket.emit('update lock', {data: {}});
    }


 });

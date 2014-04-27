 
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
            var pit = "#D00000";}
        else {
            var pit = "#080808";}

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
        var seconds = Math.round(((dt/1000) % 60) * 100)/100;
        var minutes = Math.floor(dt/60000) % 60;
        var hours = Math.floor(dt/3600000);
        $('#total_time').text(hours + ':' + minutes + ':' + seconds);
    }

 });

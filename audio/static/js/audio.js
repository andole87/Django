var prevScrollpos = $(window).scrollTop();

$(document).ready(function () {
    $('input[type="text"]').keydown(function () {
        if (event.keyCode == 13) {
            event.preventDefault();
            var param = $('#searchText').val();
            history.pushState(null, null, '/search/' + param);
            $('.container-fluid').load('/search/' + param);
        }
    })
})
function goSearch() {
    var param = $('#searchText').val();
    history.pushState(null, null, '/search/' + param);
    $('.container-fluid').load('/search/' + param);
};

$(window).scroll(function () {
    var currentScrollPos = $(window).scrollTop();
    if (prevScrollpos > currentScrollPos || prevScrollpos < 100) {
        $('.navbar.navbar-inverse').css("visibility", "visible");
    } else {
        $('.navbar.navbar-inverse').css("visibility", "hidden");
    }
    prevScrollpos = currentScrollPos;
})

$(document).ready(function () {
    $(document).on('click', '.audio a',
        function (event) {
            event.preventDefault();
            var tm = $(event.target).parent().attr('href');
            history.pushState(null, null, tm);
            $('.container-fluid').load(tm + ' .container-detail');
        })
})

$(window).on('popstate', function (event) {
    $('.container-fluid').load(location.href + ' .container-fluid');
})




// audio control
var audioList = [];
var audio;
function addList() {
    var item = $("#audiobook").data('source');
    var name = $("#audiobook").data('name');
    audioList.push([name, item]);
}


// function playAudio(){
//     if(audioList.length >0){
//         audio = new Audio(audioList[0][1]);
//         audio.play();
//         if(audio.currentTime==0){

//         }

//     }
// }

function playAudio() {
    if (audio != null) {
        pauseAudio();
    }
    audio = new Audio($("#audiobook").data('source'));
    audio.play();
    $('.navbar-fixed-bottom').css('visibility', 'visible');
    $('#currentAudio').text($('#audiobook').data('name'));
}

function pauseAudio() {
    audio.pause();
    $('.navbar-fixed-bottom').css('visibility', 'hidden');
}
function updateRunningtime(audio) {
    audio = audio;
    var currtime = 180 - Math.floor(audio.currentTime);
    return currtime;
}

function formatSecondsAsTime(int) {
    if (int == 180) {
        return "00:00";
    }
    var minutes = Math.floor(int / 60);
    var seconds = int - (minutes * 60);

    if (minutes < 10) { minutes = "0" + minutes; }
    if (seconds < 10) { seconds = "0" + minutes; }
    return minutes + ":" + seconds;
}

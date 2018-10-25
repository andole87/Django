$(document).ready(function () {
    $('input[type="text"]').keydown(function () {
      if (event.keyCode == 13) {
        event.preventDefault();
        var param = $('#searchText').val();
        window.location.href = "/search/" + param;
      }
    })
  })
  function goSearch() {
    var param = $('#searchText').val();
    window.location.href = "/search/" + param;
  };

  var prevScrollpos = $(window).scrollTop();
  $(window).scroll(function () {
    var currentScrollPos = $(window).scrollTop();
    if (prevScrollpos > currentScrollPos || prevScrollpos < 100) {
      $('.navbar navbar-inverse').css("visibility", "visible");
    } else {

      $('.navbar navbar-inverse').css("visibility", "hidden");
    }
    prevScrollpos = currentScrollPos;
  })

$(document).ready(function(){
    $(document).on('click','.audio a',
    function(event){
        event.preventDefault();
        var tm = $(event.target).parent().attr('href');
        history.pushState(null,null,tm);
        $('.container-fluid').load(tm + ' .audio');
    })
})

$(window).on('popstate', function(event){
    $('.container-fluid').load(location.href+ ' .container-fluid');
})



function playAudio(){
    var audiosrc = $('#audiobook').data('source');
    var audio = new Audio(audiosrc);
    audio.play();
}
function pauseAudio(){
    
}
function updateRunningtime(track){
    var currtime = 180 - Math.floor($('#audiobook').get(0).currentTime);
    console.log(currtime);
    $('#runningTime').text(formatSecondsAsTime(currtime));
}

function formatSecondsAsTime(int){
    if(int ==180){
        return "00:00";
    }
    var minutes = Math.floor(int/60);
    var seconds = int - (minutes*60);

    if(minutes<10){minutes = "0"+minutes;}
    if(seconds<10){seconds = "0"+minutes;}
    return minutes+":"+seconds;
}

$(function(){
    $('.nav_toggle').on('click', function () {
        $('.nav_toggle, .nav').toggleClass('show');
    });
    $('.title').hide().fadeIn(4000);


    $('#school').vegas({
        
        slides: [
            { src:'../static/kuc.jpg' },
        { src: '../static/kgc.jpg' },
        { src: '../static/duc.jpg' },
        { src:'../static/ruc.jpg'}
        ],
        delay: 4000,
        timer: false,
        transition: 'fade',


    });



  //   $('#school').bgSwitcher({
  //     images: [url('../static/kuc.jpg'),url('../static/kgc.jpg'),url('../static/duc.jpg'),url('../static/ruc.jpg')], // 切り替え画像
  //     Interval: 5000, //切り替えの間隔 1000=1秒
  //     start: true, //$.fn.bgswitcher(config)をコールした時に切り替えを開始する
  //     loop: true, //切り替えをループする
  //     shuffle: false, //背景画像の順番をシャッフルする
  //     effect: "fade", //エフェクトの種類 "fade" "blind" "clip" "slide" "drop" "hide"
  //     duration: 1000, //エフェクトの時間 1000=1秒
  //     easing: "swing", //エフェクトのイージング "swing" "linear"
  // });


$('.nav_toggle').on('click', function () {
    $('.nav_toggle, .nav').toggleClass('show');
});

    $('#1').click(function(){
        $('html, body').animate({
          'scrollTop':$('.school').offset().top
        },500);
    });

    $('#2').click(function(){
        $('html, body').animate({
          'scrollTop':$('#4').offset().top
        },800);
    });

    $('#3').click(function(){
        $('html, body').animate({
          'scrollTop':$('#5').offset().top
        },1000);
    });

    $('#ku-univ').mouseover(function(){
        $(this).attr('src','static/class.jpg');
      });
      $('#ku-univ').mouseleave(function(){
        $(this).attr('src', 'static/ku.jpg');
      });

      $('#kg-univ').mouseover(function(){
        $(this).attr('src','static/class.jpg');
      });
      $('#kg-univ').mouseleave(function(){
        $(this).attr('src', 'static/kg.jpg');
      });

      $('#du-univ').mouseover(function(){
        $(this).attr('src','static/class.jpg');
      });
      $('#du-univ').mouseleave(function(){
        $(this).attr('src', 'static/du.jpeg');
      });

      $('#ru-univ').mouseover(function(){
        $(this).attr('src','static/class.jpg');
      });
      $('#ru-univ').mouseleave(function(){
        $(this).attr('src', 'static/ru.png');
      });




}); 
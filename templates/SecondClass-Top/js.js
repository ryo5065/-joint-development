$(function(){
    $('.nav_toggle').on('click', function () {
        $('.nav_toggle, .nav').toggleClass('show');
    });
    $('.title').hide().fadeIn(4000);


    $('#school').vegas({
        
        slides: [
            { src:'img/kuc.jpg' },
        { src: 'img/kgc.jpg' },
        { src: 'img/duc.jpg' },
        { src:'img/ruc.jpg'}
        ],
        delay: 2000,
        timer: false,
        transition: 'fade',


    });

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
        $(this).attr('src', 'img/door.png');
      });
      $('#ku-univ').mouseleave(function(){
        $(this).attr('src', 'img/ku.jpg');
      });

      $('#kg-univ').mouseover(function(){
        $(this).attr('src', 'img/door.png');
      });
      $('#kg-univ').mouseleave(function(){
        $(this).attr('src', 'img/kg.jpg');
      });

      $('#du-univ').mouseover(function(){
        $(this).attr('src', 'img/door.png');
      });
      $('#du-univ').mouseleave(function(){
        $(this).attr('src', 'img/du.jpeg');
      });

      $('#ru-univ').mouseover(function(){
        $(this).attr('src', 'img/door.png');
      });
      $('#ru-univ').mouseleave(function(){
        $(this).attr('src', 'img/ru.png');
      });




}); 
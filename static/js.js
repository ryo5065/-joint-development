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

    $('#ham-menu').click(function(){
      $('#ham-menu').addClass('is-active');
      
    } );


    $('#ham-menu').click(function(){
      $('#menu-background').css( 'z-index',999);
    });
    $('#ham-menu').click(function(){
      $('#menu-background').css( 'opacity','0.3');
    });


    $('#menu-background').on('click', function(){
      if( $('#ham-menu').hasClass('is-active')){
        $('#menu-background').css( 'opacity','0');
      }
    });
  
    $('#menu-background').on('click', function(){
      if( $('#ham-menu').hasClass('is-active')){
        $('#menu-background').css( 'z-index',-999);
      }
    });
    $('#menu-background').on('click', function(){
      if( $('#ham-menu').hasClass('is-active')){
        $('#ham-menu').toggleClass('is-active');
      }
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
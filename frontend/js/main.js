 
  //Scroll-top button
  $(window).scroll(function() {
    if ($(this).scrollTop() > 100) {
      $('.scroll-icon').fadeIn('slow');
    } else {
      $('.scroll-icon').fadeOut('slow');
    }
  });

  $('.scroll-icon').click(function() {
    $('html, body').animate({
      scrollTop: 0
    }, 1500, 'easeInOutExpo');
    return false;
  });

   //Animations
   new WOW().init();
   
   AOS.init({
    offset: 400,
    duration: 1000,
});
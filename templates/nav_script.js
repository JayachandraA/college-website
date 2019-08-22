// Navigation bar
         var header = $('header');

         $(window).scroll(function() {
         var scroll = $(window).scrollTop();

         if (scroll >= 1) {
             header.addClass('header-small');
         } else {
             header.removeClass('header-small');
         }
         }).scroll();

         // Navigation bar responsive

         $(window).on('load', function() {
         $(".hamburger").on('click', function(e) {
             $(".responsive").toggleClass("nav-show");
         });
         });

         // hamburger animation

         var $hamburger = $(".hamburger");

         $hamburger.on("click", function(e) {
         $hamburger.toggleClass("is-active");
         });



         $('.trigger').on('click', function(){
            $(this).toggleClass('clicked');
         });

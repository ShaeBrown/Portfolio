/*!
 * Start Bootstrap - Grayscale Bootstrap Theme (http://startbootstrap.com)
 * Code licensed under the Apache License v2.0.
 * For details, see http://www.apache.org/licenses/LICENSE-2.0.
 */

// jQuery to collapse the navbar on scroll
$(window).scroll(function() {
    if ($(".navbar").offset().top > 50) {
        $(".navbar-fixed-top").addClass("top-nav-collapse");
    } else {
        $(".navbar-fixed-top").removeClass("top-nav-collapse");
    }
});

// jQuery for page scrolling feature - requires jQuery Easing plugin
$(function() {
    $('a.page-scroll').bind('click', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top
        }, 1500, 'easeInOutExpo');
        event.preventDefault();
    });
});

// Closes the Responsive Menu on Menu Item Click
$('.navbar-collapse ul li a').click(function() {
    $('.navbar-toggle:visible').click();
});


$(function() {
    $('a').click(function() {
        var $i =  $(this).find('i');
        if ($i.hasClass('fa-caret-right')) {
            $i.addClass('fa-caret-down');
            $i.removeClass('fa-caret-right');
        }
        else if ($i.hasClass('fa-caret-down')) {
            $i.addClass('fa-caret-right');
            $i.removeClass('fa-caret-down');
        }
    });
});

$('[data-toggle="collapse"]').click(function() 
{ 
  if ($(this).text() == "Display Code") 
  { 
     $(this).text("Hide Code"); 
  } 
  else if ($(this).text() == "Hide Code") 
  { 
     $(this).text("Display Code"); 
  }
});




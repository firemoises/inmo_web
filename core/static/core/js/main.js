/* Theme Name: Itawa - Real Estate Landing Page
	Author: Rajesh-Doot
	Version: 1.0.0
	File Description: Main JS file of the template*/
	
	/*Table of contents*/
	/*1.OWL-CAROUSEL
	2.FLOOR PLAN POPUP 
	3.GALLERY POPUP
	4.NAVBAR SCROLL
	5.Form validation */
	
(function ($) {
	"use strict";
	//OWL-CAROUSEL	
	$(".owl-carousel").each(function () {
		var $Carousel = $(this);
		$Carousel.owlCarousel({
			loop: $Carousel.data('loop'),
			autoplay: $Carousel.data("autoplay"),
			margin: $Carousel.data('space'),
			nav: $Carousel.data('nav'),
			dots: $Carousel.data('dots'),
			dotsSpeed: $Carousel.data('speed'),
			responsive: {
				0: {
					items: 1
				},
				600: {
					items: $Carousel.data('slide-res')
				},
				1000: {
					items: $Carousel.data('slide'),
				}
			}
		});
	});
	//FLOOR PLAN POPUP  
	$('.image-popup-floor-plan').magnificPopup({
		type: 'image',
		mainClass: 'mfp-with-zoom',
		gallery: {
			enabled: true
		},
	});
	//GALLERY POPUP
	$('.image-popup-gallery').magnificPopup({
		type: 'image',
		mainClass: 'mfp-with-zoom',
		gallery: {
			enabled: true
		},
	});
	//STICKY HEADER
	$(window).on('scroll', function () {
        var scroll = $(window).scrollTop();
        if (scroll < 50) {
            $(".navbar").removeClass("sticky");
        } else {
            $(".navbar").addClass("sticky");
        }
    });
	
	//NAVBAR SCROLL		
	var aScroll = $('.nav-item .nav-link'),
		$navbarCollapse = $('.navbar-collapse');
	aScroll.on('click', function (event) {
		var target = $($(this).attr('href'));
		$(this).parent(".nav-item").siblings().removeClass('active');
		$(this).parent('.nav-item').addClass('active');

		if (target.length > 0) {
			event.preventDefault();
			$('html, body').animate({
				scrollTop: target.offset().top - 70
			}, 1000);
		}
		// If click link and navabr is show
		if ($('.navbar-collapse').hasClass('show')) {
			$('.navbar-collapse').toggleClass('show');
			$('.navbar-toggler-icon').toggleClass('active');
			$('.navbar-toggler').toggleClass('collapsed');
		}
	});
	// Form validation
		// Initialize form validation on the registration form.
		// It has the name attribute "registration"
		$("form[name='feedback-form']").validate({
			// Specify validation rules
			rules: {
				// The key name on the left side is the name attribute
				// of an input field. Validation rules are defined
				// on the right side
				name: "required",
				email: {
					required: true,
					// Specify that email should be validated
					// by the built-in "email" rule
					email: true
				},
				phone: {
					required: true,
					minlength: 10
				},
				message: {
					required: true,
					minlength: 50
				}
			},
			// Specify validation error messages
			messages: {
				name: "Please enter your full name",
				phone: {
					required: "Please provide your phone number",
					minlength: "Your phone number must be at least 10 characters long"
				},
				email: "Please enter a valid email address",
				message: {
					required: "Please enter message",
					minlength: "Message must be at least 50 characters long"
				}
			},
			// Make sure the form is submitted to the destination defined
			// in the "action" attribute of the form when valid
			submitHandler: function (form) {
				form.submit();
			}
		});


})(jQuery);


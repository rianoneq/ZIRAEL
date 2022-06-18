import Swiper from 'https://unpkg.com/swiper@8/swiper-bundle.esm.browser.min.js'

//slider
let slide_images = document.querySelectorAll('.swiper-slide');
if (slide_images.length > 2) {
 

  var swiper = new Swiper(".mySwiper", {
    // loop: true,
    spaceBetween: 1,
    slidesPerView: 4,
    // freeMode: true,
    watchSlidesProgress: true,
  });
  var swiper2 = new Swiper(".mySwiper2", {
    loop: true,
    spaceBetween: 5,
    // navigation: {
    //   nextEl: ".swiper-button-next",
    //   prevEl: ".swiper-button-prev",
    // },
    thumbs: {
      swiper: swiper,
    },
  });
   
} else {
  let useless_slider = document.querySelector('.mySwiper');
  useless_slider.parentElement.removeChild(useless_slider);
}

// ??


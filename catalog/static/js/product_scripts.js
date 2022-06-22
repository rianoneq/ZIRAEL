import Swiper from 'https://unpkg.com/swiper@8/swiper-bundle.esm.browser.min.js'

//slider
let slide_images = document.querySelectorAll('.swiper-slide');
if (slide_images.length > 2) {
 

  var swiper = new Swiper('.mySwiper', {
    // loop: true,
    spaceBetween: 1,
    slidesPerView: 4,
    // freeMode: true,
    watchSlidesProgress: true,
  });
  var swiper2 = new Swiper('.mySwiper2', {
    // loop: false, 
    spaceBetween: 5,
    // navigation: {
    //   nextEl: '.swiper-button-next',
    //   prevEl: '.swiper-button-prev',
    // },
    thumbs: {
      swiper: swiper,
    },
  });
   
} else {
  let useless_slider = document.querySelector('.mySwiper');
  useless_slider.parentElement.removeChild(useless_slider);
}

// ?? здесь что то должно быть🤔

// динамическое изменение количества товаров в корзине с помощью ajax'а

function updateCartCounter() {

  $('#add_product_to_cart_btn').click(function (e) {
    
    let btn = document.querySelector('#add_product_to_cart_btn');
    const slug = btn.dataset.slug;
    let quantity = $('#id_quantity').val();

    console.log(`/cart/add/${slug}&quantity${quantity}/`);

    $.ajax({
      url: `/cart/add/${slug}&quantity=${quantity}/`,
      type: 'get',
      //data: {product_slug: slug, quantity: quantity},
      success: function (response) {
        $('.cart_total').html(response);
      },
     
    });
  });
};

updateCartCounter();
import Swiper from 'https://unpkg.com/swiper@8/swiper-bundle.esm.browser.min.js'
import getCookie from './js_funcs.js'

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
    
    let slug = this.dataset.slug;
    let quantity = $('#id_quantity').val();
    let csrf = getCookie('csrftoken');

    // console.log(`/cart/add/${slug}&quantity=${quantity}`);

    $.ajax({
      url: `/cart/add/`,
      data: {'slug': slug, 'quantity': quantity, 'csrfmiddlewaretoken': csrf},
      type: 'post',
      success: function (response) {

        if (response['success']) {
          if ($('#output_message').length > 0){
              $('#output_message').remove();
            }
          if ($('.cart_total').length > 0) {
            $('.cart_total').html(response['data']['total_count']);
          } else {
            $('#cart').append(
              `<div class="cart_total"> ${response['data']['total_count']} </div>`
            );
          }
        } else {
          if (response['data']['error']) {
            if ($('#output_message').length < 1){
              $('#output').append(`<span id='output_message' style="color: red;">${response['data']['error']}</span>`)
            }
          } 
        }
      },
     
    });
  });
};

updateCartCounter();
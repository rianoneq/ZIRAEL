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
    // loop: false, 
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

// ?? здесь что то должно быть🤔

// динамическое изменение количества товаров в корзине с помощью ajax'а

function updateCartCounter() {

  $("#add_product_to_cart_btn").click(function (e) {
    // let text = $(this.dataset.slug);
    let btn = document.querySelector("#add_product_to_cart_btn");
    const slug = btn.dataset.slug;
    // console.log(text);
    console.log("/cart/add/" + slug + '/')
    $.ajax({
      url: "/cart/add/" + slug + '/',
      type: "post",
      data: {jsdata: slug, csrfmiddlewaretoken: 'dJouZIi72bM6zIKlHhBJGWlQ9GJ0lKdqCEDblU8Zwlcg61F8bhk0gWa6cQ2y8QNO', product_slug: slug},
      success: function (response) {
        $("#out").html(response);
      },
     
    });
  });
};

updateCartCounter();
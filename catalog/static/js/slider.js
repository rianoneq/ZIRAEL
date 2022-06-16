slide_images = document.querySelectorAll('.slider_');
if (slide_images.length > 0) {
  $('#product_slider').lightSlider({
    gallery: true,
    item: 1,
    loop: true,
    slideMargin: 5,
    thumbItem: 9
  });
}
import getCookie from './js_funcs.js';

function deleteProduct() {

  $('.remove_cart_product').click(function (e) {

    let slug = this.dataset.productSlug;
    let child = this;
    let csrf = getCookie('csrftoken');

    $.ajax({
      url: `/cart/remove/`,
      data: {'slug': slug, 'csrfmiddlewaretoken': csrf},
      type: 'post',

      success: function (response) {
        // console.log(`${slug} removed! response: ${response}`);
        
        let total_price = response['total_price']
        let total_count = response['total_count']

        child.closest('.cart_product').remove();
        
        if (total_count == 0) {
          if ($('.cart_total').length > 0) {
              $('.cart_total').remove();
          };
          if ($('.total').length > 0) {
              $('.total').remove();
          };
          if ($('#create_order').length > 0) {
              $('#create_order').remove();
          };
          if ($('.cart_table').length > 0) {
              $('.cart_table').remove();
              $('#cart_text').html(
                `<span style="font-size: 22px;">
                  Ваша корзина пуста😢
                </span>`
              );
          };

          
        } else {
          if ($('.cart_total').length > 0) {
            $('.cart_total').html(total_count);
          }
          if ($('.total_price').length > 0) {
            $('.total_price').html(total_price);
          }
          
        }
      },
     
    });
  });
};

deleteProduct();
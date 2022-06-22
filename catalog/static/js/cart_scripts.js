function deleteProduct() {

  $('.remove_cart_product').click(function (e) {

    let slug = this.dataset.productSlug;
    let child = this;

    console.log(slug);

    $.ajax({
      url: `/cart/remove/${slug}`,
      type: 'get',

      success: function (response) {
        console.log(`${slug} removed! response: ${response}`);
        
        let total_price = response['total_price']
        let total_count = response['total_count']

        child.closest('.cart_product').remove();
        $('.cart_total').html(total_count);
        $('.total_price').html(total_price);
      },
     
    });
  });
};

deleteProduct();
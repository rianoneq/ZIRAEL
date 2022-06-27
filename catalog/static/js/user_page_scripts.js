function paidOrderBtnHandler() {

  $('.i_paid_order_button').click(function (e) {

    let bill_id = this.dataset.orderId;

    console.log(bill_id);

    if (bill_id.length < 1) {
      return false
    }
    $.ajax({
      url: `/orders/check/${bill_id}`,
      type: 'get',

      // success: function (response) {
      //   // console.log(`${slug} removed! response: ${response}`);
        
      //   let total_price = response['total_price']
      //   let total_count = response['total_count']

      //   child.closest('.cart_product').remove();
        
      //   if (total_count == 0) {
      //     if ($('.cart_total').length > 0) {
      //         $('.cart_total').remove();
      //     };
      //     if ($('.total').length > 0) {
      //         $('.total').remove();
      //     };
      //     if ($('#create_order').length > 0) {
      //         $('#create_order').remove();
      //     };
      //     if ($('.cart_table').length > 0) {
      //         $('.cart_table').remove();
      //         $('#cart_text').html(
      //           `<span style="font-size: 22px;">
      //             Ваша корзина пуста😢
      //           </span>`
      //         );
      //     };

          
      //   } else {
      //     if ($('.cart_total').length > 0) {
      //       $('.cart_total').html(total_count);
      //     }
      //     if ($('.total_price').length > 0) {
      //       $('.total_price').html(total_price);
      //     }
          
      //   }
      // },
     
    });
  });
};

paidOrderBtnHandler();
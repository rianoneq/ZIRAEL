function paidOrderBtnHandler() {

  $('.i_paid_order_button').click(function (e) {

    let bill_id = this.dataset.orderId;
    let button = this.parentElement;

    if (bill_id.length < 1) {
      return false
    }
    $.ajax({
      url: `/orders/check/${bill_id}`,
      type: 'get',
      success: function (response) {
        if (response['data']['status'] == 'PAID') {
          button.closest('.unpaid_order_data').remove();
          
          // call popup congrats here
          openPopup()
          
        } else {
          let all_errors = document.querySelectorAll('.error_msg'); 
          all_errors.forEach(element => {
            console.log(element)
            element.innerHTML = ''
            element.setAttribute( "style", 'border: 0px solid red;color:inherit;position:absolute;');
          });

          button.querySelector('.error_msg').setAttribute( "style", 'border: 1px solid red;position: absolute;bottom:-123%;left: -20%;color:red;font-size: 20px;width: 200px;');
          button.querySelector('.error_msg').innerHTML = 'Оплата не прошла';
        }

      },
     
    });
  });
};

paidOrderBtnHandler();


let openPopup = () => { 
    let popupBg = document.querySelector('.popup__bg'); // Фон попап окна
    let popup = document.querySelector('.popup'); // Само окно
    let openPopupButtons = document.querySelectorAll('.open-popup'); // Кнопки для показа окна
    let closePopupButton = document.querySelector('.close-popup'); // Кнопка для скрытия окна
    
    popupBg.classList.add('active'); // Добавляем класс 'active' для фона
    popup.classList.add('active'); // И для самого окна
    document.body.style.overflow = "hidden";
    
    closePopupButton.addEventListener('click',() => { // Вешаем обработчик на крестик
      popupBg.classList.remove('active'); // Убираем активный класс с фона
      popup.classList.remove('active'); // И с окна
      document.body.style.overflow = "auto";
  });

  document.addEventListener('click', (e) => { // Вешаем обработчик на весь документ
      if (e.target === popupBg) { // Если цель клика - фот, то:
          popupBg.classList.remove('active'); // Убираем активный класс с фона
          popup.classList.remove('active'); // И с окна
      }
  });
};
  
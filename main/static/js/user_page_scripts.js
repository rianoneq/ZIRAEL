import getCookie from './js_funcs.js';

let getStatus = (new_status) => {

  let statuses = {
    'Оплачен': `<span style="color:greenyellow">${new_status}</span>`,
    'Истек': `<span style="color:red">${new_status}</span>`,
    'Ожидает': `<span style="color:orange">${new_status}</span>`,
    'Ошибка': `<span style="color:red">${new_status}</span>`,
  } 

  return statuses[new_status]

}

let clearErrorMessages = (all_errors) => {
  all_errors.forEach(element => {
  
    element.innerHTML = ''
    element.setAttribute( "style", 'border: 0px solid red;color:inherit;position:absolute;');
  });
}

function paidOrderBtnHandler() {
  
  $('.i_paid_order_button').click(function (e) {
    


    let bill_id = this.dataset.orderId;
    let button = this.parentElement;
    let csrf = getCookie('csrftoken');
    let old_status = button.parentElement.parentElement.querySelector('.order__status');
    
    const eng_to_ru = {
      'PAID': 'Оплачен',
      'EXPIRED': 'Истек',
      'WAITING': 'Ожидает',
      'REJECTED': 'Ошибка',
    } 

    if (bill_id.length < 1) {
      return false
    }

    $.ajax({
      url: `/orders/check/`,

      data: {'bill_id': bill_id, 'csrfmiddlewaretoken': csrf},
      type: 'post',
      success: function (response) {
        const new_status = response['data']['status'];
        const new_status_ru = eng_to_ru[new_status]
        let all_errors = document.querySelectorAll('.error_msg'); 

        if (new_status == 'PAID') {
          button.closest('.unpaid_order_data').remove();
          let actual_status_html = getStatus('Оплачен');
          old_status.innerHTML = actual_status_html;
          
          old_status.dataset.status = 'PD';
          // call popup congrats here
          openPopup()

        } else if (old_status.textContent.trim() != new_status_ru){
          let actual_status_html = getStatus(new_status_ru);
          old_status.innerHTML = actual_status_html;
          old_status.dataset.status = new_status;
          if (new_status_ru == 'Оплачен'||new_status_ru == 'Истек') {
            button.closest('.unpaid_order_data').remove();
            clearErrorMessages(all_errors);

          }
        } else {
          clearErrorMessages(all_errors);

          button.querySelector('.error_msg').setAttribute( "style", 'border: 1px solid red;position: absolute;bottom:-123%;left: -20%;color:red;font-size: 20px;width: 200px;');
          button.querySelector('.error_msg').innerHTML = 'Оплата не прошла';
        }

      },
     
    });
  });
};

paidOrderBtnHandler();

let updateStatus = (statusElem, orderElem, new_status) => {
  let buttons = orderElem.querySelector('.unpaid_order_data');
  let statusOrder = orderElem.querySelector('.order__status');
  buttons.remove();

  let actual_status_html = NaN

  if (new_status === 'PD') {  
    actual_status_html = getStatus('Оплачен');
    statusElem.dataset.status = 'PD';
  } else if (new_status === 'EX') {
    actual_status_html = getStatus('Истек');
    statusElem.dataset.status = 'EX';
  } else {
    actual_status_html = getStatus('Ошибка');
    statusElem.dataset.status = 'RE';
  }
  statusOrder.innerHTML = actual_status_html;
}

let checkStatuses = () => {
  const statuses = document.querySelectorAll('.order__status');
  
  statuses.forEach(status => {
    const order = status.closest('.cart_product')
    const orderId = order.dataset.orderId 
    const orderStatus = status.dataset.status;

    const csrf = getCookie('csrftoken'); 
    if (orderStatus === 'WA') {

      $.ajax({
        url: '/orders/get/',

        data: {'order_id': orderId, 'csrfmiddlewaretoken': csrf},
        type: 'post',
        success: function (response) {
          if (response['success']) {
            if (response['data']) {
              if (response['data']['order_status'] === 'PD'){
                console.log(response['data']['order_status'], 'pd')

                updateStatus(status, order, response['data']['order_status'])
                // call popup congrats here
                openPopup()
              } else if (response['data']['order_status'] === 'WA'){
                // nothing
              } else {
                updateStatus(status, order, response['data']['order_status'])

              }
              
            }
          }
        }
      })

    };
  })
}

// timouts
let timerId = setInterval(() => checkStatuses(), 6000);

let openPopup = () => { 
    let popupBg = document.querySelector('.popup__bg'); // Фон попап окна
    let popup = document.querySelector('.popup'); // Само окно
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
  
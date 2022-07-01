from django.http import JsonResponse

error_list = ['Слишком много предметов в корзине!',
              'Незвестная ошибка',
              'Похоже вы не оплатили, либо заказ уже истек']

class ProcessErrors:
  def __init__(self, get_response) -> None:
    self._get_response = get_response

  def __call__(self, request) -> None:
    return self._get_response(request)

  def process_exception(self, requets, exception):
    if str(exception) in error_list:
      err = str(exception)
    else:
      err = 'Что-то пошло не так'
    return JsonResponse({
      'success': False, 
      'data': {
        'error': err
      }
    })
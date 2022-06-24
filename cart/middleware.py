from django.http import JsonResponse

class ProcessErrorProductAdd:
  def __init__(self, get_response) -> None:
    self._get_response = get_response

  def __call__(self, request) -> None:
    return self._get_response(request)

  def process_exception(self, requets, exception):
    return JsonResponse({
      'success': False, 
      'data': {
        'error': str(exception)
      }
    })
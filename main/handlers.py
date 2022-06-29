from django.core.exceptions import PermissionDenied

def is_ajax(request):
    """
      ajax detect func
    """
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest' # если этот параметр есть в METF значит это ajax запрос

def ajax_required(fn):
    """
      ajax required decorator
    """
    def wrapper(request,*args,**kwargs):
        if is_ajax(request):
            # узнаем ajax или нет по is_ajax функции
            return fn(request,*args,**kwargs) # и если все ок возвращаем контроллеру функцию обратно
        else:
            raise PermissionDenied()
    return wrapper
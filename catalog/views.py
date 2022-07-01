from django.shortcuts import render
from .models import Category, Product, PostProductImage
from cart.forms import CartAddProductForm
from django.views import generic


def index_page(request):
  return render(
    request,
    'main.html',
    {'page_title': 'Главная'}
  )


class RenderCategories(generic.ListView):
  model = Category

  def get_context_data(self, **kwargs):

    # В первую очередь получаем базовую реализацию контекста
    context = super(RenderCategories, self).get_context_data(**kwargs)
    # Добавляем новую переменную к контексту и инициализируем её некоторым значением
    context['cats'] = context['object_list']
    context['page_title'] = 'Категории'
    return context

class CategoryDetailView(generic.DetailView):
  model = Category

  def get_context_data(self, **kwargs):

    context = super(CategoryDetailView, self).get_context_data(**kwargs)
    context['page_title'] = str(context['object']) + ' | подробности о категории'
    return context

class ItemDetailView(generic.DetailView):
  model = Product

  def get_context_data(self, **kwargs):

    prod_ = Product.objects.filter(slug=self.kwargs['slug'])
    product_id = prod_[0].id
    photos = PostProductImage.objects.filter(prod=product_id)

    context = super(ItemDetailView, self).get_context_data(**kwargs)


    context['page_title'] = str(context['object']) + ' | карточка товара'
    context['cart_product_form'] = CartAddProductForm()
    
    context['images'] = photos
    return context

class RenderCatalog(generic.ListView):

  model = Product
  paginate_by = 9

  def get_context_data(self, **kwargs):
  
    context = super(RenderCatalog, self).get_context_data(**kwargs)

    context['products'] = context['object_list']
    context['page_title'] = 'Каталог'
    return context


from audioop import reverse
from django.shortcuts import render
from .models import Category, Product, PostProductImage
from django.views import generic

def index_page(request):
  return render(
    request,
    'main.html',
  )

def contacts_page(request):
  return render(
    request,
    'contacts.html',
  )


class RenderCategories(generic.ListView):
  model = Category

  def get_context_data(self, **kwargs):

    # В первую очередь получаем базовую реализацию контекста
    context = super(RenderCategories, self).get_context_data(**kwargs)
    # Добавляем новую переменную к контексту и инициализируем её некоторым значением
    context['cats'] = context['object_list']
    return context

class CategoryDetailView(generic.DetailView):
  model = Category

class ItemDetailView(generic.DetailView):
  model = Product
  def get_context_data(self, **kwargs):

    prod_ = Product.objects.filter(slug=self.kwargs['slug'])
    product_id = prod_[0].id
    photos = PostProductImage.objects.filter(prod=product_id)

    # В первую очередь получаем базовую реализацию контекста
    context = super(ItemDetailView, self).get_context_data(**kwargs)
    # Добавляем новую переменную к контексту и инициализируем её некоторым значением
    context['images'] = photos
    return context

class RenderCatalog(generic.ListView):

  model = Product
  paginate_by = 9

  def get_context_data(self, **kwargs):
  
    # В первую очередь получаем базовую реализацию контекста
    context = super(RenderCatalog, self).get_context_data(**kwargs)
    # Добавляем новую переменную к контексту и инициализируем её некоторым значением
    context['products'] = context['object_list']
    return context


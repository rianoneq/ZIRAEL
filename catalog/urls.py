from . import views
from django.urls import re_path


urlpatterns = [
    re_path(r'^$', views.index_page,
            name='index_page'),
]

urlpatterns += [
    re_path(r'^catalog/$', views.RenderCatalog.as_view(),
            name='catalog_page'),
]
urlpatterns += [
    re_path(r'^catalog/(?P<slug>[-\w]+)/$', views.ItemDetailView.as_view(),
            name='item_detail_view'),
]

urlpatterns += [
    re_path(r'^contacts/$', views.contacts_page,
            name='contacts_page'),
]

urlpatterns += [
    re_path(r'^categories/$', views.RenderCategories.as_view(),
            name='categories_page'),
]
urlpatterns += [
    re_path(r'^categories/(?P<slug>[-\w]+)$', views.CategoryDetailView.as_view(),
            name='category_detail_view'),
]


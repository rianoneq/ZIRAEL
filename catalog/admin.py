from django.contrib import admin
from .models import Category, Product, PostProductImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

class PostImageAdmin(admin.StackedInline):
    model = PostProductImage  

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]
    list_display = ['name', 'slug', 'price',
                    'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}

# @admin.register(PostProductImage)
# class PostImageAdmin(admin.ModelAdmin):
#     pass

from django.contrib import admin

from orders.models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'email', 'postal_code', 'status',
                    'created', 'updated']
    list_filter = ['status', 'created', 'updated']
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)
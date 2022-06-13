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

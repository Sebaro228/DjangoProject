# Register your models here.
# .\env1\Scripts\activate
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Product, Category
from django.utils.html import format_html
 
 
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
 
 
 
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'name', 'price', 'image_tag', 'created_at')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('created_at',)
    search_fields = ('name', 'description')
    ordering = ('-created_at',)
 
    def image_tag(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 4px" />',
                obj.image.url,
            )
        return mark_safe('<span>не має зображення</span>')
    
    image_tag.short_description = "Image"
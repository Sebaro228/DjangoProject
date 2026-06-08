from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User 
from django.contrib import admin
from django.core.validators import MinValueValidator
from django.utils.html import format_html

class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name="Ім'я категорії")
    slug = models.SlugField(max_length=50, unique=True, verbose_name="Слаг для url")
 
    
    class Meta:
        verbose_name="Категорія"
        verbose_name_plural="Категорії"
 
    def __str__(self):
        return f'{self.name}'
 
    def get_absolute_url(self):
        return reverse("main:product_list_by_category", args=[self.slug])

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True, verbose_name="Слаг для url")
    name = models.CharField(max_length=100, db_index=True)
    #перевіряй ціну на валідність, щоб не було від'ємних чисел
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='product_images/%Y/%m/%d', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукти"
    
    def __str__(self):
        return f"{self.name} - {self.price}"

    def get_absolute_url(self):
        return reverse("main:product_detail", args=[self.id, self.slug])
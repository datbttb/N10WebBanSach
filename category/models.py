from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'categories'
        ordering = ['-created_at']
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog_category', kwargs={'category_slug': self.slug})


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    image = models.ImageField(upload_to='image/', null=True)
    quantity = models.IntegerField()
    description = models.TextField(null=True)
    publisher = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category)

    class Meta:
        db_table = 'products'
        ordering = ['-created_at']

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog_product', kwargs={'product_slug': self.slug})

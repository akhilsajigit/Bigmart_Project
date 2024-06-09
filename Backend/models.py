from django.db import models


class categoriesDB(models.Model):
    Cname = models.CharField(max_length=100, null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    img_file = models.ImageField(upload_to="Categories Images", null=True, blank=True)


class ProductDB(models.Model):
    Category = models.CharField(max_length=100, null=True, blank=True)
    Product_Name = models.CharField(max_length=100, null=True, blank=True)
    Product_Price = models.IntegerField(null=True, blank=True)
    Product_Description = models.CharField(max_length=100, null=True, blank=True)
    Product_Image = models.ImageField(upload_to="Product Images", null=True, blank=True)

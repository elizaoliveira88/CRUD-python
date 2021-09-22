from django.db import models

class Stores(models.Model):
  cnpj = models.CharField(max_length=50)
  store_name = models.CharField(max_length=50)
  product_category = models.CharField(max_length=50)
  product = models.CharField(max_length=100)
  

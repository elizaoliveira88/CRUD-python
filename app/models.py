from django.db import models

CATEGORY = (
  (1,'Eletrodomésticos'),
  (2,'Eletronicos'),
  (3,'Móveis'),
)

PRODUCT = (
  (1,'Geladeira'),
  (2,'Celular'),
  (3,'Sofá'),
)



class Stores(models.Model):
  cnpj = models.CharField(max_length=50)
  store_name = models.CharField(max_length=50)
  product_category = models.CharField(
    max_length=50,
    choices=CATEGORY,
    )
  product = models.CharField(
    max_length=100,
    choices=PRODUCT,    
    )
  

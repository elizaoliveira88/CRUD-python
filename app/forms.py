from django.forms import ModelForm
from app.models import Stores

class StoresForm(ModelForm):
     class Meta:
         model = Stores
         fields = ['cnpj', 'store_name', 'product_category', 'product']


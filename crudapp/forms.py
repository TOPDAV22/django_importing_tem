from django import forms
from crudapp.models import ShopItem


class ShopItemForm(forms.ModelForm):
    class Meta:
        model  = ShopItem
        fields = [
            'itemname',
            'description',
            'price'
        ]

class ShopItemFormUpdate(forms.ModelForm):
    class Meta:
        model  = ShopItem
        fields = [
            'itemname',
            'description',
            'price'
        ]
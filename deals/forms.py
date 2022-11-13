from .models import Deal
from django.forms import ModelForm, TextInput


class DealsForm(ModelForm):
    class Meta :
        model = Deal
        fields =['item_name','price_buy','price_sell','date']

        widgets = {
            "item_name":TextInput(attrs={
                'placeholder':"Item name",
                'type':'text',
                'class':'form-control cat-typeahead typeahead',
                'autocomplete':'off',
                'data-provide':'typeahead',
                'data-source':"['ak','m4','usp','glock']"}),

            "price_buy":TextInput(attrs={
                'placeholder':"Item buy price", 
                'class':"form-control"}),

            "price_sell":TextInput(attrs={
                'placeholder':"Item sell price", 
                'class':"form-control"}),

            "date":TextInput(attrs={
                'placeholder':"Date", 
               'class':"form-control"})
            
            }

class EditDealForm(ModelForm):
    class Meta :
        model = Deal
        fields =['price_buy','price_sell']

        widgets = {
            "price_buy":TextInput(attrs={
                'placeholder':"Item buy price", 
                'class':"form-control"}),

            "price_sell":TextInput(attrs={
                'placeholder':"Item sell price", 
                'class':"form-control"})
            }

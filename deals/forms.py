from .models import Deal
from django.forms import ModelForm, TextInput,ModelChoiceField


class DealsForm(ModelForm):
    # names = Deal.objects.all().only("item_name")
    # item_name = ModelChoiceField(queryset=names, empty_label=None)
    class Meta :
        model = Deal
        fields =['item_name','price_buy','price_sell','date','item_fv']
        
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
                'required': False,
                'class':"form-control"}),

            "item_fv": TextInput(attrs={
                'placeholder': "Item fv (optional)",
                'required': False,
                'class':"form-control"}),

            "date":TextInput(attrs={
                'placeholder':"Date", 
                'class':"form-control"})
            
            }

class EditDealForm(ModelForm):
    class Meta :
        model = Deal
        fields =['price_buy','price_sell','item_fv']

        widgets = {
            "price_buy":TextInput(attrs={
                'placeholder':"Item buy price", 
                'class':"form-control"}),

            "price_sell":TextInput(attrs={
                'placeholder':"Item sell price", 
                'class':"form-control"}),

            "item_fv": TextInput(attrs={
                'placeholder': "Item fv (optional)",
                'required': False,
                'class':"form-control"})
            }


class LinkCreateDealForm(ModelForm):
    class Meta :
        model = Deal
        fields =['view_link']

        widgets = {
            "view_link":TextInput(attrs={
                'placeholder':"Item market inspect link", 
                'class':"form-control"}),
            "date":TextInput(attrs={
                'placeholder':"Date", 
                'class':"form-control"})
            }




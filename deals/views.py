from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Deal, Profit
from .forms import DealsForm, EditDealForm
from django.views.generic import DetailView
from django.db.models import Sum
from Web_app.image_parser import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


@login_required(login_url='login')
def deals(request):
    #print(request.user)
    search_bar =request.GET.get('search','')

    if search_bar:
        deals = Deal.objects.filter(author=request.user,item_name__icontains=search_bar).order_by('-date')
    else:
        deals = Deal.objects.filter(author=request.user).order_by('-date')
        all_deals = Deal.objects.all()
   
    pages = Paginator(deals, 12)
    print(pages.page_range)
    page_number = request.GET.get('page')
    page_obj = pages.get_page(page_number)

    profit = Profit.objects.filter(author=request.user)
    
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'deals/deals.html',
        {'deals':page_obj,
         'profit':profit}

    )

#/class DealsEdit(DetailView):
  #  model = Deal

   # template_name = 'deals/deal_edit.html'
   # context_object_name = 'deal_edit'


@login_required(login_url='login')
def edit(request,int):
    deal_edit = Deal.objects.get(pk=int)
    
    error_editform = ''

    if request.method =='POST':
        edit_form = EditDealForm(request.POST)
        if edit_form.is_valid():
            print(deal_edit.id)
            deal_edit.price_buy = edit_form.cleaned_data.get('price_buy')
            deal_edit.price_sell = edit_form.cleaned_data.get('price_sell')
            deal_edit.save(update_fields=["price_buy","price_sell"])
            return redirect('deals')
        else:
            error_form ="Input is not valid ! "


    edit_form = EditDealForm()
    data={
        'deal_edit' : deal_edit,
        'edit_form': edit_form,
        'error_editform': error_editform
        }

    return render(request, 'deals/deal_edit.html', data)


@login_required(login_url='login')
def sold(request,id):
    deal_sold = Deal.objects.get(pk=id)
    
    deal_sold.deal_status = True
    deal_sold.save(update_fields=['deal_status'])
    

    return redirect('deals')


@login_required(login_url='login')
def profit_calc(request):
    data = Deal.objects.filter(author=request.user)
    #profit = Deal.objects.aggregate(Sum('price_buy')) 
    #buy = profit.get('price_buy__sum')
    #print(buy)
    profit_data = Profit.objects.filter(author=request.user)
    total_buy = 0
    total_sell = 0
    total_on_sale = 0
    total_but_not_sold = 0
    for deal in data:
        if(deal.deal_status):
            total_buy += deal.price_buy
            total_sell += deal.price_sell

        elif(not deal.deal_status):
            total_but_not_sold += deal.price_buy
            total_on_sale += deal.price_sell
            

    profit_on_sale = total_on_sale - total_but_not_sold
    profit_gross = total_sell - total_buy
    
    Profit.objects.filter(author=request.user).update(profit = round(profit_gross, 2), profit_on_sale = round(profit_on_sale, 2))  
    
    return redirect('deals')


@login_required(login_url='login')
def create(request):
    error_form = ''
    img = ImageParser()
    #print(len(data))
    #deal_author = request.user
    if request.method =='POST':
        form = DealsForm(request.POST)
        
        if form.is_valid():
            form.save()
            last = Deal.objects.latest('id')
            last.author = request.user
            last.save(update_fields=["author"])
            #print(last)
            #print(last.author)
            data = Deal.objects.all()
            for item in data:
                try:
                    for name in data:
                       if(item.item_name == name.item_name and name.img != "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/2048px-No_image_available.svg.png"):
                          item.img = name.img
                          item.save(update_fields=["img"])
                          #print("saved")
                          continue
                                
                    if(item.img == "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/2048px-No_image_available.svg.png"):        
                       item.img = img.get_image(str(item.item_name))
                       #print(item.img)
                       #print("request img")
                       item.save(update_fields=["img"])

                except:
                       print(f"broken name :{item.item_name}")
               
            return redirect('deals')
        else:
            error_form ="Input is not valid ! "

    form = DealsForm()

    all_names = Deal.objects.all()
    data={
        'form': form,
        'error_form': error_form,
        'all_names': all_names
        }

    return render(request, 'deals/create.html', data)
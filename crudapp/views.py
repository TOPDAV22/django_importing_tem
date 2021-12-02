from django.shortcuts import render,redirect
from crudapp.models import ShopItem
from crudapp.forms import ShopItemForm,ShopItemFormUpdate

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.

def index(request):
    

     
    return render(request, 'crudapp/index.html')



def blog(request):
    

    
    return render(request, 'crudapp/blog.html')


def home(request):
    shopitem = ShopItem.objects.all()

    context = {
        'shopitem':shopitem
    }
    return render(request, 'crudapp/home.html', context)

def createitem(request):
    if request.method == 'POST':
        shopitemform = ShopItemForm(request.POST)
        if shopitemform.is_valid():
            shopitemform.save()
            return redirect('/')
    else:
        shopitemform = ShopItemForm()

    context = {
        'shopitemform':shopitemform
    }

    return render(request, 'crudapp/create.html', context)

def update(request, pk):
    shopitem = ShopItem.objects.get(pk=pk)
    if request.method == 'POST':
        itemupdate = ShopItemFormUpdate(request.POST, instance=shopitem)
        if itemupdate.is_valid():
            itemupdate.save()
            return redirect('/')
    else:
        itemupdate = ShopItemFormUpdate(instance=shopitem)

    context = {
        'itemupdate':itemupdate,
        
    }

    return render(request, 'crudapp/update.html', context)

def delete(request, pk):
    shopitem = ShopItem.objects.get(pk=pk)
    if request.method == 'POST':
        shopitem.delete()
        return redirect('/')

    

    return render(request, 'crudapp/delete.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('registerUsername')
        email = request.POST['registerEmail']
        password = request.POST.get('registerPassword')

        user = User.objects.create_user(
            username = username,
            email = email,
            password = password
            
        ).save()
        
        return redirect('/')
        #user.save()

    return render(request, 'crudapp/register.html')

def loginpage(request):
    if request.method == 'POST': 
        username = request.POST.get('loginUsername')
        password = request.POST.get('loginPassword')

        user = authenticate(username=username, password=password)
        if user != None:
            login(request, user)
        return redirect('/')
    return render(request, 'crudapp/login.html')
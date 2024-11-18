from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import *
# Create your views here.


def demo_login(req):
    if 'shop' in req.session:
        return redirect(shop_home)
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['password']
        data=authenticate(username=uname,password=password)
        if data:
            login(req,data)
            req.session['shop']=uname #creating a session
            return redirect(shop_home)
        else:
            messages.warning(req,'invalid username or password') #to display error message
            return redirect(demo_login)  
    else:
        return render(req,'login.html')
    
def demo_shop_logout(req):
    logout(req)
    req.session.flush() #for deleting the session
    return redirect(demo_login)
       
def shop_home(req):
    if 'shop' in req.session:
        data=Product.objects.all()
        return render(req,'shop/home.html',{'Products':data})
    else:
        return redirect(demo_login)

def add_products(req) :
    if 'shop' in req.session:
        if req.method=='POST':
            pid=req.POST['pid']
            pname=req.POST['name']
            des=req.POST['descrip']
            pprice=req.POST['price']
            oprice=req.POST['off_price']
            pstock=req.POST['stock']
            file=req.FILES['img'] #to get the img from html page we  are using file method instead of post and adding enctype in html page

            data=Product.objects.create(pid=pid,name=pname,des=des,price=pprice,offer_price=oprice,stock=pstock,img=file)
            data.save()
            return redirect(shop_home)
        else:
            return render(req,'shop/add_products.html')
    else:
        return redirect(demo_login)    
    
def edit_product(req,pid) :
        if req.method=='POST':
            proid=req.POST['proid']
            pname=req.POST['name']
            des=req.POST['descrip']
            pprice=req.POST['price']
            oprice=req.POST['off_price']
            pstock=req.POST['stock']
            file=req.FILES.get('img')
            if file:
                Product.objects.filter(pk=proid).update(pid=proid,name=pname,des=des,price=pprice,offer_price=oprice,stock=pstock,img=file)
                data=Product.objects.get(pk=pid)
                data.img=file
                data.save()
            else:  
                Product.objects.filter(pk=pid).update(pid=pid,name=pname,des=des,price=pprice,offer_price=oprice,stock=pstock,img=file)
                return redirect(shop_home)
        else:
            data=Product.objects.get(pk=pid)
            return render(req,'shop/edit_product.html',{'data':data})
            
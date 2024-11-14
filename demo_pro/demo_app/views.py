from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
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
        return render(req,'shop/home.html')
    else:
        return redirect(demo_login)
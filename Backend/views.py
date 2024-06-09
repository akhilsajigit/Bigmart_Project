from django.shortcuts import render, redirect
from Backend.models import categoriesDB, ProductDB
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from Webapp.models import ContactDB
import datetime
from django.contrib import messages


# Create your views here.

def index_page(request):
    cdate = datetime.datetime.today()
    return render(request, "index.html",{'cdate' : cdate})


def Categories_page(request):
    return render(request, "Categories.html")


def display_page(req):
    data = categoriesDB.objects.all()
    return render(req, "Display.html", {'data': data})


def save_page(req):
    if req.method == "POST":
        ca = req.POST.get('name')
        ds = req.POST.get('desc')
        fl = req.FILES['img']
        obj = categoriesDB(Cname=ca, Description=ds, img_file=fl)
        obj.save()
        messages.success(req, "Category Saved Successfully")
        return redirect(Categories_page)


def edit_categories(req, cat_id):
    data = categoriesDB.objects.get(id=cat_id)
    return render(req, "editcategories.html", {'data': data})


def update_categories(req, cat_id):
    if req.method == "POST":
        cn = req.POST.get('name')
        ds = req.POST.get('desc')
        try:
            cimg = req.FILES['img']
            fs = FileSystemStorage()
            file = fs.save(cimg.name, cimg)
        except MultiValueDictKeyError:
            file = categoriesDB.objects.get(id=cat_id).img_file
        categoriesDB.objects.filter(id=cat_id).update(Cname=cn, Description=ds, img_file=file)
    return redirect(display_page)


def delete_fun(req, cat_id):
    x = categoriesDB.objects.filter(id=cat_id)
    x.delete()
    messages.error(req,"Category Deleted")
    return redirect(display_page)


def login_page(req):
    return render(req, "Login.html")


def Admin_login(request):
    if request.method == "POST":
        un = request.POST.get('username')
        pwd = request.POST.get('password')
        if User.objects.filter(username__contains=un).exists():
            x = authenticate(username=un, password=pwd)
            if x is not None:
                login(request, x)
                request.session['username'] = un
                request.session['password'] = pwd
                messages.success(request, "WELCOME")

                return redirect(index_page)
            else:
                messages.error(request, "Invalid Password")
                return redirect(login_page)
        else:
            messages.warning(request, "User Not Found")
            return redirect(login_page)


def Admin_Logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(login_page)


def product_page(request):
    cat = categoriesDB.objects.all()
    return render(request, "Products.html", {'cat': cat})


def save_product(req):
    if req.method == "POST":
        ps = req.POST.get('p_select')
        pna = req.POST.get('p_name')
        ppr = req.POST.get('p_price')
        pd = req.POST.get('p_description')
        pimg = req.FILES['p_image']
        obj2 = ProductDB(Category=ps, Product_Name=pna, Product_Price=ppr, Product_Description=pd, Product_Image=pimg)
        obj2.save()
        return redirect(product_page)


def product_display(req):
    pdata = ProductDB.objects.all()
    return render(req, "Product_Display.html", {'pdata': pdata})


def edit_products(req, p_id):
    pdata = ProductDB.objects.get(id=p_id)
    cdata = categoriesDB.objects.all()
    return render(req, "editProducts.html", {'pdata': pdata, 'cdata':cdata})


def update_products(request, p_id):
    if request.method == "POST":
        ps = request.POST.get('p_select')
        pna = request.POST.get('p_name')
        ppr = request.POST.get('p_price')
        pd = request.POST.get('p_description')

        try:
            pimg = request.FILES['p_image']
            fs = FileSystemStorage()
            file = fs.save(pimg.name, pimg)
        except MultiValueDictKeyError:
            file = ProductDB.objects.get(id=p_id).Product_Image
        ProductDB.objects.filter(id=p_id).update(Category=ps, Product_Name=pna, Product_Price=ppr,
                                                 Product_Description=pd, Product_Image=file)
    return redirect(product_display)


def delete_pro(req, p_id):
    x = ProductDB.objects.filter(id=p_id)
    x.delete()
    return redirect(product_display)


def contact_data(req):
    data = ContactDB.objects.all()
    return render(req, "ContactData.html", {'data': data})


def delete_feedback(req, f_id):
    x = ContactDB.objects.filter(id=f_id)
    x.delete()
    return redirect(contact_data)

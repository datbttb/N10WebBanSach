from django.shortcuts import render, redirect
from category.models import Product, Category


def themsanpham(request):
    if request.method=='POST':
        loai=request.POST['theloai']
        product=Product.objects.create(name=request.POST['name'],slug=request.POST['slug'],price=request.POST['price'],image=request.FILES['image'],quantity=request.POST['so-luong'],description=request.POST['mo-ta'],publisher=request.POST['nha-cung-cap'])
        loai=Category.objects.get(slug=loai)
        product.categories.add(loai)
        product.save()
        return  redirect('/category/sanpham')
    else:
        return redirect('/')

def suasanpham(request):
    if request.method=='POST':
        product=Product.objects.get(id=request.POST['id_product'])
        product.name = request.POST['name']
        product.slug = request.POST['slug']
        product.price = request.POST['price']
        if 'image' in request.FILES and request.FILES['image']:
            product.image = request.FILES['image']
        product.quantity =request.POST['so-luong']
        product.description = request.POST['mo-ta']
        product.publisher = request.POST['nha-cung-cap']
        product.categories.clear()
        loai = Category.objects.get(slug=request.POST['theloai'])
        product.categories.add(loai)
        product.save()
        return redirect('/category/sanpham')
    else:
        return redirect('/')


def editform(request, id):
    product=Product.objects.get(id=id)
    category_list = Category.objects.all()
    return render(request, "admin/editsp.html", {"product":product, "category_list": category_list })


def getform(request):
    category_list = Category.objects.all()
    return render(request, "admin/them.html", {"category_list": category_list})

def dssanpham(request):
    sanpham_list=Product.objects.all()
    return render(request, "admin/DanhSachSanPham.html", {"sanpham_list": sanpham_list})


from django.shortcuts import render


def products_view(request):
    context = {
        'products': ['Product', 'Product 2']  # замените это на ваш список товаров
    }
    return render(request, 'E:\\312\Django\pythonProject\petMarket\my_app\my_app\\templates\product_detail.html', context)


def app(request):
    return render(request, 'product_detail.html')

def cat(request):
    return render(request, 'cats-and-dogs.html')

def dog(request):
    return render(request, 'product_detail.html')
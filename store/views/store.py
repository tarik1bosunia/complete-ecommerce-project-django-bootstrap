from django.shortcuts import render
from store.models import Product


def store_page_view(request):
    products = Product.objects.filter(is_available=True)
    context = {
        "products": products
    }
    return render(request, template_name="store/store_page.html", context=context)

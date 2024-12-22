# app_name/views.py
from django.db.models import Sum, Count
from django.http import JsonResponse
from .models import Category, Product

def get_top_categories(request):
    top_categories = (
        Category.objects.annotate(
            total_price=Sum('product__price'),
            product_count=Count('product')
        )
        .filter(total_price__gt=0)  
        .order_by('-total_price')[:5]  
    )

    result = [
        {
            "category_name": category.name,
            "total_price": category.total_price,
            "product_count": category.product_count,
        }
        for category in top_categories
    ]
    return JsonResponse(result, safe=False)

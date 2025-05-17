from django.urls import path

from .views import landingview, productlistview, supplierlistview, addsupplier, addproduct

urlpatterns = [
    path('', landingview),

    # Products url´s
    path('products/', productlistview),
    path('add-product/', addproduct),

    # Supplier url´s
    path('suppliers/', supplierlistview),
    path('add-supplier/', addsupplier),
]

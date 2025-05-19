from django.urls import path

from .views import landingview
from .views import addsupplier,deletesupplier, supplierlistview, confirmdeletesupplier, suppliers_filtered, searchsuppliers
from .views import addproduct, deleteproduct, productlistview, confirmdeleteproduct, products_filtered #searchproducts
from .views import edit_product_post, edit_product_get, edit_supplier_post, edit_supplier_get


urlpatterns = [
    path('', landingview),

    # Products url´s
    path('products/', productlistview),
    path('add-product/', addproduct),
    path('delete-product/<int:id>/', deleteproduct),
    path('confirm-delete-product/<int:id>/', confirmdeleteproduct),
    # path('search-products/', searchproducts),
    path('products-by-supplier/<int:id>/', products_filtered),
    path('edit-product-get/<int:id>/', edit_product_get),
    path('edit-product-post/<int:id>/', edit_product_post), 

    # Supplier url´s
    path('suppliers/', supplierlistview),
    path('add-supplier/', addsupplier),
    path('delete-supplier/<int:id>/', deletesupplier),
    path('confirm-delete-supplier/<int:id>/', confirmdeletesupplier),
    path('search-suppliers/', searchsuppliers),
    path('suppliers-by-supplier/<int:id>/', suppliers_filtered),
    path('edit-supplier-get/<int:id>/', edit_supplier_get),
    path('edit-supplier-post/<int:id>/', edit_supplier_post),
]

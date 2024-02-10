from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', include("frontend.urls")),
    path('admin/', admin.site.urls),
    path("products/",include("products.urls")),
    path("orders/",include("orders.urls")),
    path("companies/",include("companies.urls")),
    path("categories/",include("categories.urls")),
    path("auth/",include("users.urls")),
]

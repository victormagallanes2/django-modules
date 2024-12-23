from django.urls import path
from .views import ProductsListAPI
from .views import ProductsDetailAPI
from .views import ProductsCreateAPI
from .views import ProductsUpdateAPI
from .views import ProductsDeleteAPI


urlpatterns = [            
               path('products/list/', ProductsListAPI.as_view()),
               path('products/create/', ProductsCreateAPI.as_view()),
               path('products/detail/<str:pk>/', ProductsDetailAPI.as_view()),
               path('products/update/<str:pk>/', ProductsUpdateAPI.as_view()),
               path('products/delete/<str:pk>/', ProductsDeleteAPI.as_view()),
               ]
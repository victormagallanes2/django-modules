from django.urls import path
from .views import Home, ProductsByCategory


urlpatterns = [            
               path('', Home.as_view(), name='home'),
               path('category/<int:id>/', ProductsByCategory.as_view(), name='products_by_category'),
               ]
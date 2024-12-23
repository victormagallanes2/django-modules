from django.views.generic import ListView
from pure_pagination.mixins import PaginationMixin
from django_modules.products.models import Products, Category


class Home(PaginationMixin, ListView):
    template_name = 'index.html'
    model = Category
    paginate_by = 16


class ProductsByCategory(ListView):
    model = Products
    template_name = 'productsbycategory.html'

    def get_queryset(self):
        self.category = Category.objects.get(id=self.kwargs['id'])
        return Products.objects.filter(category=self.category)
from django.urls import reverse_lazy
from .models import Product
from django.views.generic import ListView, DeleteView,CreateView
from .forms import ProductForm

class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'product_list.html'
    context_object_name = 'products'

class ProductDetailView(DeleteView):
    queryset = Product.objects.all()
    template_name = 'product_detail.html'
    context_object_name = 'product'

class ProductCreateView(CreateView):
    template_name = 'product_create.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_list')





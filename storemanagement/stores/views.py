from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from .models import *
from .forms import *
# Create your views here.
def index(request):
	return render(request, 'index.html')

def display_product(request):
	items=Product.objects.all()
	context={
	'items':items
	}

	return render(request, 'index.html', context)	


def add_product(request):
	if request.method == "POST":
		form = ProductForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('index')

	else:
		form =ProductForm(request.POST)
		return render(request, 'add_new.html', {'form':form})


def edit_product(request, pk):
	item = get_object_or_404(Product, pk=pk)

	if request.method == 'POST':
		form = ProductForm(request.POST, instance=item)
		if form.is_valid():
			form.save()
			return redirect('index')

	else:
		form = ProductForm(instance=item)
		return render(request, 'edit_product.html', {'form':form})	

def sell_product(request, pk):
	item = get_object_or_404(Product, pk=pk)
	if request.method == 'POST':
		form = UpdateProduct(request.POST, instance=item)
		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form = UpdateProduct(instance=item)
		return render(request, 'sell_product.html', {'form':form})		


def delete_product(request, pk):
	Product.objects.filter(id=pk).delete()

	items = Product.objects.all()

	context={
	'items':items
	}

	return render(request, 'index.html', context)

class HomePageView(TemplateView):
    template_name = 'index.html'

class SearchResultsView(ListView):
    model = Product
    template_name = 'search_results.html'

    def get_queryset(self): # new
       query = self.request.GET.get('q')
       items=Product.objects.filter(Q(prod_name__icontains=query) | Q(company__icontains=query) | Q(prod_type__icontains=query))
       return items


def get_stock(request):
	items=Product.objects.filter(units__lte=2)

	context={
	'object_list': items
	}

	return render(request, 'UpdateStock.html', context)


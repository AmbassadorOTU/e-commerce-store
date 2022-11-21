from django.shortcuts import render
from store.models import Collection, Customer, Product


def index(request):
    # queryset = Product.objects.select_related('collection').all()
    collection = Collection(pk=13)
    # collection.title = 'Another test create'
    # collection.featured_product = Product(pk=3)
    collection.delete()
    # collection.save()

    return render(request, 'index.html', {'name': 'Uchechi'})

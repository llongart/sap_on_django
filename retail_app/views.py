from django.shortcuts import render
from .forms import ZinvtdForm

# Create your views here.
def stock(request):
    # if request.method == "POST":
    form = ZinvtdForm(request.POST)

        # if form.is_valid(): 

    return render(request, 'stock/zinvtd.html', {
        'title': 'ZINVTD | Stock de artículos',
        'subtitle': 'Stock en tienda',
        'form': form
    })
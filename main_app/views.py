from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main_app/index.html', {
        'title': 'Inicio'
    })

def admin(request):
    return render(request, 'main_app/admin.html')

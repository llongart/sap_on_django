from django.http import HttpResponse
from django.shortcuts import render
from .forms import ZinvtdForm, MatchCodeForm

# Create your views here.
def stock(request):
    form = ZinvtdForm()
    return render(request, 'stock/zinvtd.html', {
        'title': 'ZINVTD | Stock de artículos',
        'subtitle': 'Stock en tienda',
        'form': form
    })

def material_matchcode(request):
    # matchcode = MatchCodeForm()
    # return render(request, 'stock/matchcode.html', {
    #     'title': 'Matchcode',
    #     'matchcode': matchcode
    # })    
    response = """
            <div>
                <label for="id_material">Artículos:</label>
                <textarea name="material" cols="40" rows="10" class="articles_matchcode_form" placeholder="Artículos" id="id_material">
                </textarea>
            </div>
    """
    return HttpResponse(response)

def article_grp_matchcode(request):  
    response = """
            <div>
                <label for="id_article_grp">Grupo de artículos:</label>
                <textarea name="articles_grp" cols="40" rows="10" class="articles_grp_matchcode_form" placeholder="Grupo de artículos" id="id_articles_grp">
                </textarea>
            </div>
    """
    return HttpResponse(response)
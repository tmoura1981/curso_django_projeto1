from django.shortcuts import render


# Create your views here.
def home(request):
    # home.html é tudo o que será redenrizado
    # estando dentro da pasta templates, uma subpasta de Recipes
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Thiago'
    })

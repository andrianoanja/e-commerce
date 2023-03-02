from django.shortcuts import render, get_object_or_404,redirect
from site_web.models import Produit,Categorie,Panier,Article,Profile
from django.core.paginator import Paginator
from django.views import View
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def index(request):
    produits = Produit.objects.all()
    item_name = request.GET.get('item-name')
    if item_name != '' and item_name is not None:
        produits = Produit.objects.filter(designation__icontains=item_name)
    pagination = Paginator(produits, 4)
    page = request.GET.get('page')
    produits = pagination.get_page(page)
    return render(request, 'store/index.html', {'produits' : produits})

def produit_detail(request, myid):
    produit = get_object_or_404(Produit, id=myid)
    return render(request, 'store/detail.html', context={'produit': produit})

class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'compte/register.html', {'form': form})
    
    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()  
        return redirect('index')
    
    
def produit(request):
    produits = Produit.objects.all()
    return render(request, 'store/produits.html', {'produits' : produits})


def categories(request):
    categories = Categorie.objects.all()
    return render(request, 'store/categories.html', {'categories':categories})


def categori(request, myid):
    category = get_object_or_404(Categorie, id=myid)
    produits = Produit.objects.filter(categorie=category)
    categories = Categorie.objects.all()
    context = {
        'category': category,
        'produits': produits,
        'categories': categories,
    }
    return render(request, 'store/categor-prod.html', context)


@login_required
def ajout_panier(request,myid):
    user = request.user
    produit = get_object_or_404(Produit, id=myid)
    panier, _ = Panier.objects.get_or_create(user=user)
    article, created = Article.objects.get_or_create(user=user,produit=produit)
    
    if created:
        panier.articles.add(article)
        panier.save()
    else:
        article.quantite += 1
        article.save()
    return redirect('index')

@login_required
def panier(request):
    panier = get_object_or_404(Panier, user=request.user)
    context = {"articles":panier.articles.all()}
    return render(request,'store/panier.html', context)

@login_required
def suprimer_article(request,myid):
    suprimer = Article.objects.get(id=myid).delete()
    return redirect('panier')
  
@login_required  
def suprimer_panier(request):
    if panier := request.user.panier:
        panier.articles.all().delete()
        panier.delete()
    return redirect('index')


@login_required
def plus_quantite(request, myid):
    if request.method == 'GET':
        qte = get_object_or_404(Article, id=myid)
        qte.quantite += 1
        qte.save()
    return redirect('panier')

@login_required
def moins_quantite(request, myid):
    if request.method == 'GET':
        qte = get_object_or_404(Article, id=myid)
        qte.quantite -= 1
        if qte.quantite == 0:
            qte = Article.objects.get(id=myid).delete()
            return redirect('panier')
        qte.save()
    return redirect('panier')

@login_required
def profile(request):
    return render(request,'compte/profile.html')
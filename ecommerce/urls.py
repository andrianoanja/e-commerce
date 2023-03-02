"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from ecommerce import settings
from site_web.views import index, produit_detail,produit,categories, categori,ajout_panier,panier,suprimer_article,suprimer_panier,plus_quantite,moins_quantite,profile
from site_web import views
from django.contrib.auth import views as auth_views
from site_web.forms import LoginForm,PasswordChangeForm
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index,name="index"),
    path('produits/', produit,name="produit"),
    path('produit?id=<int:myid>/', produit_detail, name="produit"),
    path('produit?id=<int:myid>/ajout_panier/', ajout_panier, name="ajout-panier"),
    path('panier/',panier,name="panier"),
    path('suprimer_article?id=<int:myid>/',suprimer_article,name="suprimer-article"),
    path('suprimer_panier',suprimer_panier,name="suprimer-panier"),
    path('plus-qte/<int:myid>/', plus_quantite, name="plus"),
    path('moins-qte/<int:myid>/', moins_quantite, name="moins"),
    path('compte/register/', views.RegistrationView.as_view(), name="register"),
    path('accounts/password-change/', auth_views.PasswordChangeView.as_view(template_name='compte/changer-mdp.html', form_class=PasswordChangeForm, success_url='password-change-succ/'), name="password-change"),
    path('accounts/password-change/password-change-succ/', auth_views.PasswordChangeDoneView.as_view(template_name='compte/mdpmodif.html'), name="password-change-done"),
    path('categories/', categories, name="categories"),
    path('categorie/<int:myid>',categori,name="categori"),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='compte/login.html', authentication_form=LoginForm,next_page='index'), name="login"),
    path('compte/deconnexion/', auth_views.LogoutView.as_view(next_page='index'), name="logout"),
    path('profile/',profile,name="profile"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

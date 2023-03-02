from django.contrib import admin
from site_web.models import Categorie, Produit, Adresse, Article, Panier, Profile


# Register your models here.
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('designation','prix','description','categorie','image')
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('categorie', 'description', 'image')
class AdresseAdmin(admin.ModelAdmin):
    list_display = ('user','localisation','commune','district','province')

class PanierAdmin(admin.ModelAdmin):
    list_display = ('utilisateur','produit','quantite')

admin.site.register(Produit,ProduitAdmin)
admin.site.register(Adresse,AdresseAdmin)
admin.site.register(Categorie,CategorieAdmin)
admin.site.register(Article)
admin.site.register(Panier)
admin.site.register(Profile)
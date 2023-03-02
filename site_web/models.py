from django.db import models
from django.contrib.auth.models import User
import decimal

# Create your models here.
class Adresse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    localisation = models.CharField(max_length=100)
    commune = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    province = models.CharField(max_length=100)

    def __str__(self):
        return  self.localisation

class Categorie(models.Model):
    categorie = models.CharField(max_length=90)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to ="categories", blank=True, null=True)

    def __str__(self):
        return self.categorie

class Produit(models.Model):
    designation = models.CharField(max_length=100)
    prix = models.FloatField(default=0.0)
    description = models.TextField(blank=True, null=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="produits",blank=True,null=True)

    def __str__(self):
        return self.designation

class Article(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    produit=models.ForeignKey(Produit,on_delete=models.CASCADE)
    quantite=models.PositiveIntegerField(default=1)
    commande=models.BooleanField(default=False)
    date_commande=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.produit.designation} ({self.quantite})"
        
    @property
    def total(self):
        return self.quantite * self.produit.prix
   
class Panier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    articles=models.ManyToManyField(Article)
    
    def __str__(self):
        return self.user.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(max_length=200, blank=True)
    biography = models.TextField(blank=True)
    telephone = models.CharField(max_length=20, blank=True)
    photo = models.ImageField(
        upload_to='photo de profile',
        blank=True,
        null=True
    )
    def __str__(self):
        return self.user.username
    
from django.db import models
from django.contrib.auth.models import User

#Class pour les informations sur l'utilisateur
class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)#Liaison vers le User
    #Informations compplémentaire à ajouter
    
    def __str__(self):
        return "Profil de {}".format(self.user.username)


class Post(models.Model):
    pseudo = models.CharField(max_length=42, verbose_name='Pseudo')
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    content = models.TextField(null=True, verbose_name='Contenu')
    id_profil = models.IntegerField()
    is_visible = models.BooleanField(verbose_name='publié?', default=True)
    #comments = models.ManyToManyField(CommentPost)
    #Les pseudos des personnes qui postent sont forcément connecté et on les recupère ainsi
    #ajout d'une catégorie?
    #Un model commun parent à Post et commentPost?
    def __str__(self):
        return "Post : {}".format(self.title)


class CommentPost(models.Model):
    pseudo = models.CharField(max_length=42, verbose_name='Pseudo')
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    content = models.TextField(null=True, verbose_name='Postez votre propre commentaire :')
    is_visible = models.BooleanField(verbose_name='publié?', default=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    #Ajouter id article pour plus de sécurité
    def __str__(self):
        return "Commentaire de {}".format(self.post.title)
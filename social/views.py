from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Profil, Post, CommentPost
from .forms import ConnexionForm, CommentForm
from django.contrib.auth.models import User


def connexion(request):
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
            else: # sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'social/connexion.html', locals())

def deconnexion(request):
    logout(request)
    return redirect(connexion)

def homepage(request):
    profils = Profil.objects.order_by('id')
    return render(request, 'social/homepage.html', locals())

@login_required
def wall(request, id_profil, id_post=0):
    #On sélectionne le mur dont l'id à été choisi
    try:
        profil = Profil.objects.get(id=id_profil)
    except Profil.DoesNotExist:
        raise Http404
    #---------------------------------------------
    #On affiche les posts du profils et leurs commentaires attachés
    posts = Post.objects.filter(id_profil=id_profil, is_visible=True).order_by('-date')
    comments = CommentPost.objects.filter(is_visible=True).order_by('-date')
    #--------------------------------------------- 
    #On affiche le formulaire pour rajouter des commentaires
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            commentaire = CommentPost()
            commentaire.pseudo = request.user.username
            commentaire.content = form.cleaned_data["content"]
            commentaire.post = Post.objects.get(id=id_post)
            commentaire.save()
            form = CommentForm()#pour initialiser le formulaire à vide!!
    else:
        form = CommentForm()
    #---------------------------------------------    
    return render(request,'social/wall.html',{'profil':profil, 'posts':posts, 'comments':comments, 'form':form})#'form':form, comment:....

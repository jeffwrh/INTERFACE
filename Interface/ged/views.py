from django.shortcuts import render, get_object_or_404
from .models import Fichier, Dossier
from django.http import HttpResponse
from django.views.generic import ListView


def index():
    return HttpResponse('Hello Django')


def new_dossier(request):
    return HttpResponse('Hello Django')


# Affichage de la liste des dossiers
def dossiers(request):
    dossier = Dossier.objects.all().order_by('Nom_Dossier')
    return render(request, 'liste_dossier.html', {'dossier':dossier})


# Affichage du contenu du dossier
class DossierFichierList(ListView):
    template_name = 'cont_dossier.html'

    def get_queryset(self):
        self.dossier = get_object_or_404(Dossier, Nom_Dossier=self.kwargs['dossier'])
        return fichier.objects.filter(dossier=self.dossier)


# Affichage brut de la liste des fichiers
def liste(request):
    fichier = Fichier.objects.all()
    return render(request, 'liste_fichier.html', {'fichier': fichier})


# Affichage de la liste des fichiers trié par dossiers
def tri(request):
    fichier = Fichier.objects.all().order_by('Status')
    return render(request, 'liste_fichier.html', {'fichier': fichier})

from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste),
    path('liste', views.liste),
    path('dossiers', views.dossiers),
    path('liste_Ordo', views.tri),
    path('new_dossier', views.new_dossier),
    path('fichier/<dossier>/', views.DossierFichierList),
]

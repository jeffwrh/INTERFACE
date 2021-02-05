from django.contrib import admin
from .models import Dossier, Fichier, Commentaires, Status


class DossierAdmin(admin.ModelAdmin):
    list_display = ('Nom_Dossier', 'Description')


class FichierAdmin(admin.ModelAdmin):
    list_display = ('Nom_Fichier', 'Nom_Dossier', 'Date', 'Heure', 'Origine', 'Objet', 'Fichier', 'Observations')


class CommentairesAdmin(admin.ModelAdmin):
    list_display = ('Nom_Fichier', 'Comment')


class StatusAdmin(admin.ModelAdmin):
    list_display = ('Status', 'Desc_Status')


admin.site.register(Dossier, DossierAdmin)
admin.site.register(Fichier, FichierAdmin)
admin.site.register(Commentaires, CommentairesAdmin)
admin.site.register(Status, StatusAdmin)
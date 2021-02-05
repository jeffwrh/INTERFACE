from django.db import models


class Dossier(models.Model):
    Nom_Dossier = models.CharField(max_length=50, unique=True)
    Description = models.CharField(max_length=2000)

    def __str__(self):
        return self.Nom_Dossier


class Status(models.Model):
    Status = models.CharField(max_length=20, null=False, blank=False, unique=True)
    Desc_Status = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.Status


class Fichier(models.Model):
    Nom_Dossier = models.ForeignKey('Dossier', on_delete=models.CASCADE)
    Nom_Fichier = models.CharField(max_length=80, null=False, blank=False, unique=True)
    Date = models.DateField()
    Heure = models.TimeField()
    Origine = models.CharField(max_length=20, default='CDO')
    Objet = models.CharField(max_length=200)
    Fichier = models.FileField(upload_to='.static/Fichiers', null=True, blank=True)
    Version = models.PositiveIntegerField(default=0)
    Status = models.ForeignKey('Status', on_delete=models.PROTECT)
    Observations = models.CharField(max_length=2000, null=True, blank=True)
    Createur = models.CharField(max_length=50, null=False, blank=False)
    Valideur = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.Nom_Fichier


class Commentaires(models.Model):
    Nom_Fichier = models.ForeignKey('Fichier', on_delete=models.CASCADE)
    Comment = models.CharField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return str(self.Nom_Fichier)

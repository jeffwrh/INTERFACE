# Generated by Django 3.1.5 on 2021-01-29 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dossier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom_Dossier', models.CharField(max_length=50, unique=True)),
                ('Description', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status', models.CharField(max_length=20, unique=True)),
                ('Desc_Status', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Fichier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom_Fichier', models.CharField(max_length=80, unique=True)),
                ('Date', models.DateField()),
                ('Heure', models.TimeField()),
                ('Origine', models.CharField(default='CDO', max_length=20)),
                ('Objet', models.CharField(max_length=200)),
                ('Fichier', models.FileField(blank=True, null=True, upload_to='.static/Fichiers')),
                ('Version', models.PositiveIntegerField(default=0)),
                ('Observations', models.CharField(blank=True, max_length=2000, null=True)),
                ('Createur', models.CharField(max_length=50)),
                ('Valideur', models.CharField(blank=True, max_length=50, null=True)),
                ('Nom_Dossier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ged.dossier')),
                ('Status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ged.status')),
            ],
        ),
        migrations.CreateModel(
            name='Commentaires',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Comment', models.CharField(blank=True, max_length=2000, null=True)),
                ('Nom_Fichier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ged.fichier')),
            ],
        ),
    ]
# Generated by Django 5.1.3 on 2024-11-25 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_fournisseur', '0003_rename_tel1_fournisseur_tel'),
    ]

    operations = [
        migrations.AddField(
            model_name='fournisseur',
            name='i_f',
            field=models.CharField(default='Pending', max_length=20),
        ),
        migrations.AddField(
            model_name='fournisseur',
            name='numrc',
            field=models.CharField(default='Pending', max_length=20),
        ),
    ]

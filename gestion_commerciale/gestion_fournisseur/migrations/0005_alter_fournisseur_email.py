# Generated by Django 5.1.3 on 2024-12-04 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_fournisseur', '0004_fournisseur_i_f_fournisseur_numrc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fournisseur',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]

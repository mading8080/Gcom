# Generated by Django 5.1.3 on 2024-12-06 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('idclient', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('numrc', models.CharField(default='Pending', max_length=20)),
                ('i_f', models.CharField(default='Pending', max_length=20)),
                ('adresse', models.CharField(max_length=255)),
                ('ville', models.CharField(max_length=100)),
                ('tel', models.CharField(max_length=15, unique=True)),
                ('tel2', models.CharField(blank=True, max_length=15, null=True)),
                ('fax', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True, unique=True)),
                ('date_creation', models.DateField()),
            ],
            options={
                'db_table': 'client',
                'ordering': ['nom'],
            },
        ),
    ]

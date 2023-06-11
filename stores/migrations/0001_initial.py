# Generated by Django 4.2.2 on 2023-06-11 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('disponibilé', models.BooleanField(default=True)),
                ('address', models.CharField(max_length=255)),
                ('zone', models.CharField(max_length=100)),
                ('rgion', models.CharField(max_length=100)),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('heur_ouverture', models.CharField(default='08.00', max_length=4)),
                ('heur_fermeture', models.CharField(default='20.00', max_length=4)),
                ('jour_repos', models.CharField(choices=[('L', 'lundi'), ('M', 'mardi'), ('Me', 'mercredi'), ('J', 'jeudi'), ('V', 'vendredi'), ('D', 'samedi'), ('D', 'dimanche')], max_length=10)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
# Generated by Django 2.2.10 on 2020-05-10 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compte', '0003_auto_20200510_0448'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='status',
            field=models.CharField(choices=[('en attente', 'en attente'), ('En cours de livraison', 'En cours de livraison'), ('livraison', 'livraison')], max_length=200, null=True),
        ),
    ]

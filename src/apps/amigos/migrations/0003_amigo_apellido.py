# Generated by Django 3.2.6 on 2021-08-20 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amigos', '0002_alter_amigo_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='amigo',
            name='apellido',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

# Generated by Django 5.0.2 on 2024-02-12 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='img',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]

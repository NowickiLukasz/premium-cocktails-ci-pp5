# Generated by Django 3.2 on 2022-10-10 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_alter_recipeingredient_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredient',
            name='unit',
            field=models.CharField(choices=[('ML', 'ML'), ('OZ', 'OZ')], max_length=50),
        ),
    ]

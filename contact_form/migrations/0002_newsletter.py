# Generated by Django 3.2 on 2022-09-22 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_form', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('created_on', models.DateField(auto_now_add=True)),
            ],
        ),
    ]

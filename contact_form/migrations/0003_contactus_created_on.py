# Generated by Django 3.2 on 2022-09-22 13:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contact_form', '0002_newsletter'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='created_on',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

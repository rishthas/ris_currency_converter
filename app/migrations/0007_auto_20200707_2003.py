# Generated by Django 3.0.8 on 2020-07-07 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200707_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='profil_pic',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]

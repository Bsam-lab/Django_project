# Generated by Django 5.1.6 on 2025-03-06 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_delete_veggie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vegie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('offer', models.CharField(max_length=100)),
                ('rate', models.CharField(max_length=50)),
            ],
        ),
    ]

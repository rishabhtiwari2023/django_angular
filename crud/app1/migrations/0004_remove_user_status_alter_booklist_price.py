# Generated by Django 5.0.2 on 2024-03-01 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='status',
        ),
        migrations.AlterField(
            model_name='booklist',
            name='price',
            field=models.CharField(max_length=150),
        ),
    ]

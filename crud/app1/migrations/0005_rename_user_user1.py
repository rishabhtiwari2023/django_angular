# Generated by Django 5.0.2 on 2024-03-01 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_remove_user_status_alter_booklist_price'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='User1',
        ),
    ]

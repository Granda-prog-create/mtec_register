# Generated by Django 5.0.3 on 2024-03-12 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_options_alter_user_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Usuário', 'verbose_name_plural': 'Usuários'},
        ),
    ]

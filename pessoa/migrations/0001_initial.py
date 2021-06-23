# Generated by Django 3.2.4 on 2021-06-22 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('telefone', models.CharField(max_length=11, verbose_name='Telefone')),
                ('email', models.CharField(max_length=100, unique=True, verbose_name='Email')),
            ],
            options={
                'db_table': 'pessoa',
            },
        ),
    ]

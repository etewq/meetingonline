# Generated by Django 5.1.4 on 2024-12-24 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('icon', models.FileField(upload_to='images/', verbose_name='Иконка')),
            ],
            options={
                'verbose_name': 'Интерес',
                'verbose_name_plural': 'Интересы',
            },
        ),
        migrations.CreateModel(
            name='DatingProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
                ('bio', models.TextField(verbose_name='Описание анкеты')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Фотография')),
                ('date_birth', models.DateField(verbose_name='Дата рождения')),
                ('interests', models.ManyToManyField(related_name='profile', to='main.interest')),
            ],
            options={
                'verbose_name': 'Анкета',
                'verbose_name_plural': 'Анкеты',
            },
        ),
    ]

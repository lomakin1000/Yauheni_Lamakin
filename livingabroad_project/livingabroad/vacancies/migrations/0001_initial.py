# Generated by Django 4.1 on 2022-08-17 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('salary', models.CharField(max_length=20, verbose_name='Salary')),
                ('description', models.TextField(verbose_name='Description')),
                ('remote', models.CharField(max_length=20, verbose_name='Remote')),
                ('link', models.URLField(verbose_name='Link')),
                ('city', models.CharField(max_length=50, verbose_name='City')),
            ],
        ),
    ]
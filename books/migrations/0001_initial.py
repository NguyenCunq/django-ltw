# Generated by Django 4.1.3 on 2022-11-02 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('author', models.CharField(max_length=200, null=True)),
                ('category', models.CharField(max_length=200, null=True)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('page', models.IntegerField(null=True)),
                ('description', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]

# Generated by Django 5.0.6 on 2024-05-18 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('User_Email', models.EmailField(blank=True, max_length=100, null=True)),
                ('User_Password', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]

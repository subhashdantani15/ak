# Generated by Django 4.2.4 on 2023-08-19 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_userregister_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.IntegerField()),
                ('message', models.TextField()),
            ],
        ),
    ]

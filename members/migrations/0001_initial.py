# Generated by Django 3.2 on 2021-04-20 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MemberModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('birth', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('avatar', models.ImageField(upload_to='')),
                ('mobile', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=50)),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]

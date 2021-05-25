# Generated by Django 3.2 on 2021-05-25 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactFileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='ContactsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('loc', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=20)),
                ('contents', models.TextField()),
                ('created', models.DateField(auto_now_add=True)),
                ('files', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact', to='contacts.contactfilemodel')),
            ],
            options={
                'verbose_name_plural': 'CONTACTS',
            },
        ),
    ]

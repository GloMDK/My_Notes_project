# Generated by Django 4.0.4 on 2022-04-20 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='app_portfolio/images/')),
            ],
        ),
    ]

# Generated by Django 4.0 on 2024-02-15 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20)),
                ('message', models.TextField()),
                ('seened', models.BooleanField(default=False)),
            ],
        ),
    ]

# Generated by Django 5.2 on 2025-04-16 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecruiterProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('company_description', models.TextField()),
                ('website', models.URLField(blank=True, null=True)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
    ]

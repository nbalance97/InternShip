# Generated by Django 2.2.5 on 2021-07-18 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InterestCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('intern_title', models.CharField(max_length=100)),
                ('duration', models.DateTimeField()),
            ],
        ),
    ]

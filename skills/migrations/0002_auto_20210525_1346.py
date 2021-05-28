# Generated by Django 3.0 on 2021-05-25 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('roll', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('message', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='StudentData',
        ),
    ]